class Dog():
    """A simple attempt to model a dog"""
    num_dogs = 0

    def __init__(self, name, age):
        """initialize name and attributes"""
        Dog.num_dogs = Dog.num_dogs + 1
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

print(Dog.num_dogs)
my_dog = Dog('willie', 6)
print(Dog.num_dogs)
your_dog = Dog('lucy', 8)
print(Dog.num_dogs)



print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
