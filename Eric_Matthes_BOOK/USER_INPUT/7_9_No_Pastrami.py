sandwich_orders = ['tuna sandwich', 'pastrami','turkey sandwich',
                   'pastrami', 'salami sandwich', 'pastrami']
print(sandwich_orders)
print("\nThe dali has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)