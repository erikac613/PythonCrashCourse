print("Enter two numbers and I will add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = raw_input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = raw_input("\nSecond Number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add a number and letters!")
    else:
        print(answer)
