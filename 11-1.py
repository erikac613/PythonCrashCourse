from city_functions import city_country

print("Enter 'q' at any time to quit.")
while True:
    city = raw_input("\nPlease enter the name of a city: ")
    if city == 'q':
        break
    country = raw_input("Please enter the name of the country where that city is located: ")
    if country == 'q':
        break
    formatted_city_and_country = city_country(city, country, population='')
    print("\tNeatly formatted location: " + formatted_city_and_country + ".")
