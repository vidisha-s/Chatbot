
import random

def chatbot(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"])

    elif "how are you" in user_input:
        return "I am fine! How are you?"

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot."

    elif "machine learning" in user_input:
        return "Machine Learning enables computers to learn from data."

    elif "python" in user_input:
        return "Python is a popular programming language used in AI and ML."

    elif "help" in user_input:
        return "Sure! Ask me anything related to my predefined rules."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Please try another question."


print("Chatbot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
