import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
INTENTS_FILE = os.getenv('INTENTS_FILE')
MODEL_FILE = os.getenv('MODEL_FILE')
WORDS_FILE = os.getenv('WORDS_FILE')
CLASSES_FILE = os.getenv('CLASSES_FILE')
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