# a = int(input('Введите число '))
# b = a % 2
# # c = a / 10
# # d = a // 10
# print('b = a % 2 is ', b)
# # print('c = a / 10', c)
# # print('d = a // 10', d)

## exception handling - check for string
# user_input = input('Enter the number between 1 and 12: ')
# while (not user_input.isdigit()):
#    print('That is not a number')

## check for even and odd numbers
# n = 100
# evens = []
# odds = []
# for i in range(n + 1):
#     if not i % 2:
#         evens.append(i)
#     else:
#         odds.append(i)

##превращает список в строку
#new_phrase = "".join(plist)

## reverse string short way
# word = input('Enter a word: ')
# print(word[::-1])

## generate 100 random integers
# import random
# for i in range(100):
#     print(random.randint(1, 100), end='')

## open webpage
# import webbrowser
# webbrowser.open('https://docs.python.org/3/library/index.html')

## Sort the list in reverse order
#my_list.sort(reverse=True)

## Efficient fill of list comprehension
# squares = [value**2 for value in range(1, 11)]
# print(squares)

## copy lists
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_foods[:]

## example of if for loop / list checking for empty list
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

## Efficient list generation
#numbers = list(range(1,10))

## KeyError example
# alien_0 = {'color': 'green', 'points': 5}
# del alien_0['points']
# print(alien_0)
# print(alien_0['points'])