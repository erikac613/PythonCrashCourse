prompt = "\nEnter a topping you would like on your pizza. "
prompt += "When you are finished adding toppings, enter 'quit' to exit.\n\t"
message = " "

while message != 'quit':
    message = raw_input(prompt)

    if message != 'quit':
        print(message)
