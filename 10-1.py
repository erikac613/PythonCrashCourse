filename = 'learning_python.txt'

with open(filename) as file_object:
    #contents = file_object.read()
    #print(contents)
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
