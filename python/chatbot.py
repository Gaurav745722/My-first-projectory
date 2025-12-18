import openai
import os

# Load API key from environment variable (correct usage)
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4o" if available
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def start_chatbot():
    """Handles chatbot conversation loop"""
    print("🤖 Chatbot started! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chatbot()
