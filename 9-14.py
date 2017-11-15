from random import randint


class Die(object):

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, sides):
        roll_outcome = randint(1, sides)
        print(roll_outcome)

my_roll = Die(20)
my_roll.roll_die(20)
