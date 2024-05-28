{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi there", "How are you", "Is anyone there?", "Hey", "Hola", "Hello", "Good day"],
      "responses": ["Hello", "Good to see you again", "Hi there, how can I help?"],
      "context_set": ""
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"],
      "responses": ["See you!", "Have a nice day", "Bye! Come back again soon."],
      "context_set": ""
    },
    {
      "tag": "thanks",
      "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
      "responses": ["My pleasure", "You're welcome."],
      "context_set": ""
    },
    {
      "tag": "complex_query",
      "patterns": ["Can you explain quantum computing?", "What are the latest trends in AI?", "I need a detailed analysis on cloud security."],
      "responses": ["Let me think about that for a moment."],
      "context_set": "complex_response"
    },
    {
      "tag": "partnership_inquiry",
      "patterns": ["We're interested in a partnership.", "How can our company collaborate with you?", "What are the requirements for becoming a partner?"],
      "responses": ["We're always looking to build new partnerships. What type of collaboration are you interested in?", "Great! Let's talk about how we can work together. What's your business focus?"],
      "context_set": "partnership_discussion"
    },
    {
      "tag": "partnership_area_specification",
      "patterns": ["What areas can we collaborate on?", "Are there specific sectors you're interested in for partnerships?"],
      "responses": ["We're particularly interested in technology, healthcare, and education sectors. What's your company's specialty?"],
      "context_filter": "partnership_discussion",
      "context_set": "partnership_area_discussion"
    },
    {
      "tag": "partnership_terms_discussion",
      "patterns": ["Can we discuss the terms of the partnership?", "What are the usual conditions for a partnership with your company?"],
      "responses": ["Sure, we can discuss terms. We typically start with a pilot project. Does that work for you?"],
      "context_filter": "partnership_discussion",
      "context_set": "partnership_terms_discussion"
    },
    {
      "tag": "end_partnership_discussion",
      "patterns": ["Thank you, that's all I needed to know about partnerships.", "No more questions, thanks for the information on partnerships."],
      "responses": ["You're welcome! If you have any more questions in the future or wish to proceed with a partnership, feel free to contact us.", "Glad I could help! Don't hesitate to reach out for further information."],
      "context_filter": "partnership_discussion",
      "context_set": ""
    },
    {
      "tag": "service_customization_followup",
      "patterns": ["I'm interested in custom software development", "Do you provide customizations for existing products?"],
      "responses": ["Yes, we offer custom software development services tailored to your needs. Can you tell me more about your project requirements?", "Absolutely, we can customize our existing products to better suit your needs. What modifications are you considering?"],
      "context_filter": "service_customization_discussion",
      "context_set": "service_customization_details"
    },
    {
      "tag": "end_service_customization_discussion",
      "patterns": ["That's all I wanted to know about customization, thanks.", "No more questions about customization."],
      "responses": ["You're welcome! If you have any more questions or decide to proceed with a customization project, just let us know.", "Glad to provide the information. We're here when you're ready to start your customization project."],
      "context_filter": "service_customization_discussion",
      "context_set": ""
    },
    {
      "tag": "bulk_order_discounts",
      "patterns": ["How much is the discount for bulk orders?", "What's the rate for ordering in large quantities?"],
      "responses": ["The discount for bulk orders depends on the quantity ordered. For orders above 100 units, we offer a 10% discount, and for orders above 500 units, the discount is 15%.", "For large quantity orders, we provide scaled discounts. Starting at 10% for 100+ units, and increasing to 15% for orders of 500 units or more."],
      "context_filter": "bulk_order_discussion",
      "context_set": "bulk_order_discount_details"
    },
    {
      "tag": "end_bulk_order_discussion",
      "patterns": ["Thanks for the bulk order info", "Got all the information I needed about bulk orders."],
      "responses": ["You're welcome! If you need any more information or are ready to place a bulk order, feel free to reach out.", "Great, we're here to help when you decide to proceed with your bulk order. Thanks for inquiring!"],
      "context_filter": "bulk_order_discussion",
      "context_set": ""
    },
    {
      "tag": "technical_support_procedure",
      "patterns": ["What's the process for getting technical support?", "How do I report a problem with my product?"],
      "responses": ["For technical support, you can contact us directly via email or phone. We also have a support ticket system on our website for tracking your issue.", "To report a problem, please use our support ticket system or reach out through our contact page. Our technical team will assist you as soon as possible."],
      "context_filter": "technical_support_discussion",
      "context_set": "technical_support_details"
    },
    {
      "tag": "end_technical_support_discussion",
      "patterns": ["That answers my technical support question, thanks.", "No more questions about support."],
      "responses": ["You're welcome! If you encounter any issues or have further questions, our support team is here to help.", "Great, don't hesitate to contact us if you need technical support in the future. Have a good day!"],
      "context_filter": "technical_support_discussion",
      "context_set": ""
    }
  ]
}
