sandwich_orders = ['roast beef', 'tuna', 'ham and cheese', 'falafel', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("Making sandwich: " + current_order)
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
