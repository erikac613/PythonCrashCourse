rivers = {'nile': 'egypt', 'thames': 'england', 'yellow': 'china', 'mississippi': 'north america', 'danube': 'austria'}
#for river, country in rivers.items():
#    print("The " + (river.title()) + " runs through " + (country.title()) + ".")
for river in rivers.keys():
    print("\nThe names of the rivers are as follows: " + river.title())

for country in rivers.values():
    print("\n and the countries are as follows: " + country.title())
