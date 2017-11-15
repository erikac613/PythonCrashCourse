import json

filename = 'fave_num.json'

with open(filename) as file_object:
    fave_num = json.load(file_object)

print("I know your favorite number! It's " + str(fave_num) + "!")    
