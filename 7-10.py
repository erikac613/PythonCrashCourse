places = {}

polling_active = True

while polling_active:
    name = raw_input("\nWhat is your name? ")
    place = raw_input("If you could take a vacation anywhere, where would you go? ")

    places[name] = place

    repeat = raw_input("\nWould you like to let someone else reply? yes/no ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name, place in places.items():
    print(name + " would like to visit " + place)
