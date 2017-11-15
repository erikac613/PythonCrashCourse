def city_country(city_name, country_name):
    city_country_pair = city_name + ", " + country_name
    return city_country_pair.title()

location = city_country('dublin', 'ireland')
print(location)
location = city_country('toronto', 'canada')
print(location)
location = city_country('auckland', 'new zealand')
print(location)
