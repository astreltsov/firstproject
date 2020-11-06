# age = input("Please enter your age: ")
# age = int(age)
# if age <= 3:
#     print("you can come for free")
# elif age > 3 and age <= 12:
#     print("your price is $10")
# else:
#     print("your price is $15")

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")