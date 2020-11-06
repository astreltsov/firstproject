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

## Конвертация ['c'] в с
#s = " ".join(languages)

## import 100 random integers
# import random
# for i in range(100):
#     print(random.randint(1,100), end=' ')

## Remove spaces from text
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery ' \
#            'The five orange pips The man with the twisted lip The adventure of the blue ' \
#            'carbuncle The adventure of the speckled band '
# new_words = sherlock.split(' ')
# for i in range(len(new_words)):
#     new_words[i] = new_words[i].split('\n')
# print(new_words)

## Count each letter in a text
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# letter_count = {}
# for letter in sherlock:
#     letter_count[letter.lower()] = letter_count.get(letter,0) + 1
#     #print(letter_count)
# #letter_count['m'] = 1
# #print(letter_count)
# letter_count_clean = {}
# for k, v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k] = v
# print(letter_count_clean)

## join two lists and unjoin
# my_list_1 = [1, 2, 3, 4]
# my_list_2 = ['a', 'b', 'c', 'd', 'e']
#
# joined = list(zip(my_list_1, my_list_2))
# print(joined)

# i, j = zip(*joined)
# print(i)
# print(j)

## make every word as an item in the list
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# new_words = sherlock.split(' ')
# print(new_words)

## strip method - removes character, space, etc.
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# new_words = sherlock.split(' ')
# print(new_words)
# for i in range(len(new_words)):
#     new_words[i] = new_words[i].strip('y')
# print(new_words)

##lists within the lists
# my_list = [[1, 2, 3], [4,5,6], [7,8,9]]
# print(my_list[1][1])

## count letters using collection Counter method
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# from collections import Counter
# print(Counter(sherlock.lower()))

## dictionary comprehension
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# from collections import Counter
# print(Counter(sherlock.lower()))
# new_dict = dict(Counter(sherlock.lower()))
# new_dict = {k:v for k, v in new_dict.items() if k.isalpha()}
# print(new_dict)

## Fibonnacci number sequence
# n = 20
# a = 0
# b = 1
# fib_num = []
# for i in range(n):
#     fib_num.append(a)
#     a,b = b,a+b
# print(fib_num)

## print unique values from the dictionary. Checking for repeats. Set method
# favorite_languages = { -- snip --}
# for language in set(favorite_languages.values()):
#     print(language)

## dictionary within dictionary dynamic population
# companies =['PDS', 'PST', 'PZN', 'PB']
# k = ['Open', 'High', 'Low', 'Close']
# v = [[12.87, 13.23, 11.42, 13.10], [23.54, 25.76, 21.87, 22.33],
#      [98.99, 102.34, 97.21, 100.065], [203.63, 207.54, 202.43, 205.24]]
# d = {}
# for i in range(len(k)):
#     d[companies[i]] = dict(zip(k,v[i]))
# print(d)

## day count until the holiday
# import datetime
# today = datetime.date.today()
# print(f"Today's date is {today}.")
# holiday = datetime.date(2020,12,31)
# delta = holiday - today
# print(f"Just {delta.days} days until the holiday")

## using the flag Active
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

## while True loop break command
# prompt = "\nPlease enter the name of the city: "
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

## Example of continue command
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

## Store input in dictionary
# name_prompt = "Enter your name: "
# place_prompt = "\nEnter place "
# repeat_prompt = "\nDo you have any other favourite places? (Yes/No)"
#
# responses = {}
#
# while True:
#     name = input(name_prompt)
#     place = input(place_prompt)
#     #store the results
#     responses[name] = place
#     #check for more answers
#     repeat = input(repeat_prompt)
#     if repeat != 'yes':
#         break
# #Show the results of the survey
# print(f"\n ---- The results are: ---- ")
# for name, place in responses.items():
#     print(f"{name.title()} would like to visit {place.title()}")

##function formatted name
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)