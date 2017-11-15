sandwich_orders = ['pastrami', 'roast beef', 'pastrami', 'tuna', 'ham and cheese', 'pastrami', 'falafel', 'turkey']
finished_sandwiches = []

print(sandwich_orders)

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("Making sandwich: " + current_order)
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
