import random

# define some greetings
greetings = ["hello", "hi", "hey"]

# define some responses
responses = ["How are you?", "Nice to meet you!", "What can I do for you?"]

# start the conversation
print("Bot: Hi there! How can I assist you?")

# loop to continue the conversation
while True:
    # get user input
    user_input = input("You: ").lower()
    
    # check if user wants to end the conversation
    if user_input in ["bye", "goodbye", "exit"]:
        print("Bot: Goodbye! Have a nice day.")
        break
    
    # check if user greets the bot
    if user_input in greetings:
        bot_response = random.choice(responses)
        print("Bot:", bot_response)
    else:
        print("Bot: I'm sorry, I didn't understand what you said.")
