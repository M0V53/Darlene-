import google.generativeai as genai

AI_KEY = "AIzaSyDh4J1TQ23b3P6MrQ7cW3Q88-43nLV_fh4"

genai.configure(api_key=AI_KEY)

def chatbot(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Welcome to the Gemini Pro Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        bot_response = chatbot(user_input)
        print(f"Bot: {bot_response}")