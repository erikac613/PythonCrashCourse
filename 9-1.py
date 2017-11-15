class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

restaurant = Restaurant('pho hoa binh', 'vietnamese')
print("My favorite restaurant is " + restaurant.restaurant_name.title() + ".")
print("I love " + restaurant.cuisine_type.title() + " food!")
restaurant.describe_restaurant()
restaurant.open_restaurant()
