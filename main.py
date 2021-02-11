import random

#Simple chat program





def init_chat():
  quit_character = 'q'
  print("If you want to quit press the 'q'  key, \nif not, ")
  print("Hello, my name is Choppo, today I will be focusing on you, what is your name?")
  user_input = input()
  print("Nice to meet you " + str(user_input) + "!")

  def generate_response(user_input):
    responses = ["anything else", "why", "How are you now?", "Interebesting, let's talk about something new, your choice, start talking about it now"]

    responses_2 = [
      "How are you?",
      "!",
      "You don't say!",
      "Very cool!",
      "Programming is fun!"
    ]

    return random.choice(responses)


  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")


if __name__ == "__main__":
  init_chat()














'''

  def generate_response(user_input):
    responses = [
      "How interesting!",
      "You don't say!",
      "Very cool!",
      "Programming is fun!"
    ]
    
    
    for i in responses:
      return responses[i]   






      if user_input == str("Choppo") or str("choppo"):
    print("Hey we have he same name!\n")
  else:
    print("We have different names")
  print("Nice to meet you " + str(user_input) + "!\n")

'''