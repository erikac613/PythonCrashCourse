filename = 'learning_python.txt'

with open(filename) as file_object:
    message = "learning python is fun!"
    new_message = message.replace('python', 'java')
    print(message)
    print(new_message)
