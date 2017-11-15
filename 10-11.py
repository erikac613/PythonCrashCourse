import json

number = raw_input("What is your favorite number? ")

filename = 'fave_num.json'
with open(filename, 'w') as file_object:
    json.dump(number, file_object)
