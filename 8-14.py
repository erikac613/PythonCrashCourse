def car_profile(manufacturer, model, **car_info):
    profile = {}
    profile['car manufacturer'] = manufacturer
    profile['car model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_data = car_profile('hyundai', 'elantra gt', color='silver', mileage='19,000')

print(car_data)        
