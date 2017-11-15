class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

this_restaurant = Restaurant('pho hoa binh', 'vietnamese')
that_restaurant = Restaurant('starlight diner', 'korean')
other_restaurant = Restaurant('two stick', 'sushi')

this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()

that_restaurant.describe_restaurant()
that_restaurant.open_restaurant()

other_restaurant.describe_restaurant()
other_restaurant.open_restaurant()
