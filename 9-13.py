from collections import OrderedDict

actual_dictionary = OrderedDict()

actual_dictionary['sort'] = 'permanently store list of items alphabetically'
actual_dictionary['reverse'] = 'reverse the order of a list'
actual_dictionary['len'] = 'find the length of a list'
actual_dictionary['slice'] = 'a specific group of items in a list'
actual_dictionary['tuple'] = 'a list of immutable values'

#print("The definition of sort is: " + actual_dictionary['sort'] + ".")
#print("\nThe definition of reverse is: " + actual_dictionary['reverse'] + ".")
#print("\nThe definition of len is: " + actual_dictionary['len'] + ".")
for word, definition in actual_dictionary.items():
    print("\nWord: " + word)
    print("\nDefinition: " + definition)
