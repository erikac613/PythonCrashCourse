cities = {'atlanta': {'country': 'united states', 'population': '450,000', 'fact': 'home of the 1996 olympic games'}, 'auckland': {'country': 'new zealand', 'population': '1.3 million', 'fact': 'built on an extinct volcano'}, 'toronto': {'country': 'canada', 'population': '2.6 million', 'fact': 'most linguistically diverse city in canada'}}

for city, info in cities.items():
    print("\nCity: " + city.title())
    country_info = info['country']
    pop_info = info['population']
    fun_fact = info['fact']

    print("Country: " + country_info.title())
    print("Approximate Population: " + pop_info)
    print("Fun Fact: " + fun_fact)
