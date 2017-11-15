filename = 'pi_digits.txt'

with open(filename) as file_object:
    #contents = file_object.read()
    #print(contents.strip())

    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
