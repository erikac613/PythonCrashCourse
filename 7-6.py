prompt = "\nEnter a topping you would like on your pizza. "
prompt += "When you are finished adding toppings, enter 'quit' to exit.\n\t"
message = " "

active = True
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:    
        print(message)
