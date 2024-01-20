import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def create_chatbot(messages):
    # Generate a chat-based response using OpenAI API
    response = openai.Completion.create(
        engine="davinci-codex",
        messages=messages,
        max_tokens=150  # Adjust as needed
    )

    return response.choices[0].text.strip()

def main():
    print("Welcome to the Business Chatbot!")

    instructions = "You are a helpful assistant to a gas station. M-F hours are 24/7. Saturday hours are 8am-11pm. On sunday everything is closed. The car wash is open M-F only between 8am-6pm. There is a no more coca cola in stock today."
    conversation_history = [{"role": "system", "content": instructions}]  # Initialize conversation history

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Add user input to the ongoing conversation
        conversation_history.append({"role": "user", "content": user_input})

        # Get the chatbot's response
        chatbot_response = create_chatbot(conversation_history)

        # add response to ongoing conversation
        conversation_history.append({"role": "assistant", chatbot_response})

        print("Chatbot:", chatbot_response)

if __name__ == "__main__":
    main()
