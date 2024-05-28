import json
import numpy as np
import nltk
import requests
import logging
import asyncio
import aiohttp
from tensorflow.keras.models import load_model
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from config import API_KEY, INTENTS_FILE, MODEL_FILE, WORDS_FILE, CLASSES_FILE

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the lemmatizer and load the necessary data
lemmatizer = WordNetLemmatizer()
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Load model and data
try:
    with open(INTENTS_FILE) as file:
        intents = json.load(file)
    words = pickle.load(open(WORDS_FILE, 'rb'))
    classes = pickle.load(open(CLASSES_FILE, 'rb'))
    model = load_model(MODEL_FILE)
except Exception as e:
    logging.error(f"Error loading data or model: {e}")
    raise

def clean_up_sentence(sentence):
    """Tokenize and lemmatize the input sentence."""
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    """Convert sentence into bag-of-words representation."""
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    """Predict the class of the input sentence."""
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list

async def call_llm_async(text):
    """Call the large language model asynchronously for complex queries."""
    async with aiohttp.ClientSession() as session:
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'text-davinci-002',
            'prompt': text,
            'max_tokens': 150
        }
        try:
            async with session.post('https://api.openai.com/v1/completions', headers=headers, json=payload) as response:
                response.raise_for_status()
                result = await response.json()
                return result['choices'][0]['text']
        except aiohttp.ClientError as e:
            logging.error(f"Error contacting LLM service: {e}")
            return "Sorry, I'm having trouble understanding right now. Please try again later."

def update_context(user_id, tag, intents_json):
    """Update the user context based on the current intent."""
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            if 'context_set' in intent:
                sessions[user_id]['context'] = intent['context_set']
            elif 'context_clear' in intent:
                sessions[user_id].pop('context', None)

async def get_response(tag, intents_json, text):
    """Generate a response based on the predicted intent or call LLM if needed."""
    if tag == 'complex_query':
        return await call_llm_async(text)
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

async def main():
    """Main function to handle incoming messages."""
    while True:
        message = input("Enter your message: ")
        tag = predict_class(message)[0]['intent']
        response = await get_response(tag, intents, message)
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
