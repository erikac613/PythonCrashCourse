age = raw_input("\nPlease enter your age for ticket price: ")

age = int(age)

if age < 3:
    print("Your ticket is free!")
if age <= 12:
    print("Your ticket is $5.")
if age > 12:
    print("Your ticket is $12.")
