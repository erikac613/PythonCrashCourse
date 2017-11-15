pets = {'spike': {'animal': 'bearded dragon', 'owner': 'steve'}, 'princess': {'animal': 'poodle', 'owner': 'candee'}, 'ted': {'animal': 'lop-eared rabbit', 'owner': 'brandon'}, 'mewcifer': {'animal': 'black cat', 'owner': 'damien'}, 'polly': {'animal': 'parrot', 'owner': 'chad'}}

for pet, pet_info in pets.items():
    print("\nPet Name: " + pet.title())
    pet_type = pet_info['animal']
    pet_owner = pet_info['owner']

    print("Type of Animal: " + pet_type.title())
    print("Owner's Name: " + pet_owner.title())
