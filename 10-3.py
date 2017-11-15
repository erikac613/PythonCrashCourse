filename = 'guest.txt'

with open(filename, 'w') as file_object:
    prompt = "\n Please enter your name: "
    prompt += "\n(Enter 'quit' when you are finished.)"

    while True:
        guest_name = raw_input(prompt)
        message = "\nThank you for signing the guest book, " + guest_name + "."
        if guest_name == 'quit':
            break
        else:
            file_object.write(message)
