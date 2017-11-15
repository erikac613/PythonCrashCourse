import json

def favorite_number():
    filename = 'fave_num.json'
    try:
        with open(filename) as file_object:
            fave_num = json.load(file_object)
    except IOError:
        number = raw_input("What is your favorite number? ")
        with open(filename, 'w') as file_object:
            json.dump(number, file_object)
    else:
        print("I know your favorite number! It's " + str(fave_num) + "!")
