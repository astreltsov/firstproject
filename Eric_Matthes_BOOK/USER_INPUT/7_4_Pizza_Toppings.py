prompt = "Please enter your pizza toppings: "
prompt += "\n(Enter 'quit' to stop )"
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Topping {topping} was added to your pizza")
    else:
        break