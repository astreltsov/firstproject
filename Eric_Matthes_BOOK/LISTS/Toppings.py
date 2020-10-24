# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}")
# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepporoni', 'pineapple', 'extra cheese']
reguested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for reguested_topping in reguested_toppings:
    if reguested_topping in available_toppings:
        print(f"Adding {reguested_topping}")
    else:
        print(f"Sorry, we don't have {reguested_topping}.")
print("\nFinished making your pizza!")
