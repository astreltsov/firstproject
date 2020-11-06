capitals = {
    'France': 'Paris',
    'Spain': 'Madrid',
    'United Kingdom': 'London'
}
#print('Moscow' in capitals)
user_input = input('Which country would you like to check?:> ')
user_input = user_input.lower()
while ('United Kingdom' not in user_input and not user_input.isalpha()):
    if user_input == 'USA':
        break
    print('You must input a string')
    user_input = input('Which country would you like to check?:> ')
user_input = user_input.title()
print(user_input)
if user_input in capitals:
    print(f"The capital of {user_input} is {capitals[user_input]}")
else:
    print('No data available')