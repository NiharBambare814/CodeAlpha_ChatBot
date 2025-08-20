def chatbot_response(user_input):
    input_clean = user_input.lower()
    if input_clean == "hello":
        return "Hi!"
    elif input_clean == "how are you":
        return "I'm fine, thanks!"
    elif input_clean == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understood that."

print("----- ChatBot -----")
print("Type something ('hello','how are you' OR say 'bye' to exit):")
while True:
    msg = input("You: ")
    reply = chatbot_response(msg)
    print("Bot:", reply)
    if msg.lower() == "bye":
        break

