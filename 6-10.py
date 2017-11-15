favorite_numbers = {'sarah': ['7', '14'], 'george': ['55', '13', '22'], 'erika': ['13', '42'], 'gabby': ['21'], 'caleb': ['420', '33', '0']}

for name, numbers in favorite_numbers.items():
    if len(numbers) >= 2:
        print("\n" + name.title() + "'s favorite numbers are:")
    else:
        print("\n" + name.title() + "'s favorite number is:")
    for number in numbers:
        print(number)
