# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += "\nWhat is your name?:> "
# name = input(prompt)
# print(f"\nHello, {name}!")

# num = input('Enter a number: ')
# num = int(num)
# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# prompt = "\nPlease enter the name of the city: "
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #store the response in the dictionary
    responses[name] = response
    #find out if anyone else is going to take the poll
    repeat= input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#Polling is complete
print("\n --- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")