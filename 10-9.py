def open_files(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except IOError:
        pass

filename = 'cats.txt'
open_files(filename)
filename = 'birds.txt'
open_files(filename)
filename = 'dogs.txt'
open_files(filename)
