filename = 'why_program.txt'

with open(filename, 'a') as file_object:
    prompt = "Why do you love programming? "
    prompt += "\n(Please enter'quit' to exit.) "

    while True:
        reason_why = raw_input(prompt)
        message = "\n" + reason_why
        if reason_why == 'quit':
            break
        else:
            file_object.write(message)
