def describe_city(city_name, country_name = 'canada'):
    print(city_name.title() + " is in " + country_name.title() + ".")

describe_city('toronto')
describe_city(city_name = 'ottowa')
describe_city(city_name = 'dublin', country_name = 'ireland')
