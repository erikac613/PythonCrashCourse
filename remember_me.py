import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except IOError:
        return None
    else:
        return username

def get_new_username():
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct_user = raw_input("Is " + username + " the correct username? Enter yes or no: ")
        if correct_user == 'yes':
            print("Welcome back, " + username + "!")
        elif correct_user == 'no':
            get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
