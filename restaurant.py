class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def number_of_customers(self):
        print("This restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, tables):
        self.number_served += tables

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'mint chip', 'strawberry', 'caramel']

    def list_flavors(self):
        print("We have the following flavors today: " + str(self.flavors))
