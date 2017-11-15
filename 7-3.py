number = raw_input("Enter a number, and I will tell you if it is a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by ten.")
else:
    print("\nThe number " + str(number) + " is not a multiple of ten.")
