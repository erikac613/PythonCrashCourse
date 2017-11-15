from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
first = ' '
last = ' '
while True:
    input1 = raw_input("\nPlease enter a first name: ")
    if input1 == 'q':
        break
    else:
        first = input1
    input2 = raw_input("Please enter a last name: ")
    if input2 == 'q':
        break
    else:
        last = input2

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
