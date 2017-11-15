my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = my_foods[:]
for food in my_foods:
    print(food.title())

friend_foods.append('salad')

for food in friend_foods:
    print(food.title())   
