class Car():
    wheels = 4
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo_reading = 0

    def car_info(self):
        print("My car is a " + str(self.year) + " " + self.make.title() + " " + self.model.title() + ".")

print(Car.wheels)

my_car = Car('honda', 'cr-v', 2000)

my_car.car_info()
