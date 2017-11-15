class Cat():
    """My attempt to model some cats I know"""

    def __init__(self, name, age, breed):
        """Initialize name and attributes"""
        self.name = name
        self.age = age
        self.breed = breed

    def play(self):
        """Simulate a cat playing with its toys"""
        print(self.name.title() + " is playing with a ball of yarn!")

    def glare(self):
        """Simulates that look I know all too well"""
        print(self.name.title() + " gives you a thousand-mile stare.")

my_cat = Cat('skells', 12, 'maine coon')
moms_cat = Cat('bonnie jack', 8, 'calico')

print("My cat's name is " + my_cat.name.title() + ".")
print(my_cat.name.title() + " is " + str(my_cat.age) + " years old.")
print(my_cat.name.title() + " is a " + my_cat.breed.title() + ".")
my_cat.play()

print("\nMy mom's cat's name is " + moms_cat.name.title() + ".")
print(moms_cat.name.title() + " is " + str(moms_cat.age) + " years old.")
print(moms_cat.name.title() + " is a " + moms_cat.breed.title() + ".")
moms_cat.glare()
