import itertools, random

deck = list(itertools.product(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], ['Hearts', 'Diamonds', 'Clubs', 'Spades']))

random.shuffle(deck)
print ("You got: ")
for i in range(5):
    return [i][0], [i][1]
