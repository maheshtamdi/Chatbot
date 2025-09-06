# main.py
from nlp_model import NLPModel
from api_integration import get_weather, get_joke
from data_utils import analyze_chat_data

def run_chatbot():
    # Example training data
    X_train = ["hello", "hi", "weather in London", "tell me a joke"]
    y_train = ["greeting", "greeting", "weather", "joke"]

    # Train NLP model
    chatbot = NLPModel()
    chatbot.train(X_train, y_train)

    # Simple chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break

        intent = chatbot.predict(user_input)

        if intent == "greeting":
            print("Bot: Hello! How can I help you today?")
        elif intent == "weather":
            print("Bot:", get_weather("London"))  # Example: London fixed
        elif intent == "joke":
            print("Bot:", get_joke())
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    run_chatbot()
    # Example of using data analysis utility
    # analyze_chat_data("chat_data.csv")
