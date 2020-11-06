sandwich_orders = ['tuna sandwich', 'turkey sandwich', 'salami sandwich']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
print("\nThe following sandwiches were made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")