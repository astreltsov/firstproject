# a = int(10)
# b = int(input('введите цену '))
# if b <= a:
#    b = b * 0.9
#    print('ваша цена соскидкой ', b)
# else:
#    b = b * 0.8
#    print('ваша цена соскидкой ', b)

# n = int(input('введите число '))
# f = 1
# for i in range(1, n + 1):
# f *= i
# *=	x *= 3	x = x * 3
#    f = f*i
# print(f)
# a = 547
# b = a % 10
# c = (a // 10) % 10
# x = a // 100
# print(x, c, b)
# ********************

# import math
# a = int(input('Введите начальное число '))
# b = int(input('Введите конечное число '))
# for i in range(a , b+1):
#    s = math.sqrt(i)
#    if int(s) == s:print(s)
# **************************

# d = int(input('Введите число '))
# x = int(input('Введите цифру '))
# l = str(d)
# b = len(l)
# print(b)
# a = 0
# s = 0
# for i in range(a , b)
# n1 = d % 10 if n1 = x: s = s + 1
# d = d // 10
# n2 = d % 10 if n2 = x: s = s + 1
# d = d // 10
# n3 = d % 10 if n3 = x: s = s + 1
# print(n1, n2, n3)
# print(s)

# print('how are\n\tyou today?')

# far = float(input('Enter temp in Fahrenheit: '))
# cel = (far - 32) * 5/9
# print(far, 'Far in Cels is', cel)

# x = 5
# y = 6
# print('x = ',x, 'y = ',y)
# print(x > y)

# a, b, c = 1, 2, 3
# print(a, b, c)
# print(a < 5 and b > 5)

# a = str(input('Enter the number between 1 and 5: '))
# a = a.lower()
# if a == 'one':
#      print(1)
# elif a == 1:
#     print('one')
# elif a == 2:
#     print('two')
# elif a == 3:
#     print('three')
# elif a == 4:
#     print('four')
# else:
#     print('You entered the number that is outside the range')

# a = 6
# b = int(input('Guess a number: '))
# if b > a:
#     print('Your guess is too high')
# elif b < a:
#     print('Your guess is too low')
# else:
#     print('You are right')

# your_name = str(input('Pls enter your name: -> '))
# l = len(your_name)
# #print(l)
# if l > 5:
#     print('Your name is', l, 'char long')
# else:
#     print('Secret')

# a = int(input('Enter the number between 1 - 20 : '))
# b = int(input('Enter the number between 1 - 20 : '))
# if a > 15 and b > 15:
#     print(a * b)
# #elif (a > 15 and b < 15) or (a < 15 and b > 15):
# elif a > 15 or b > 15:
#     print(a + b)
# else:
#     print(0)

# a = int(input('Enter the number: '))
# b = int(input('Enter the number: '))
# a, b = b, a
# print(a)
# print(b)

# for i in range(0, 101, 4):
#      print(i, end=' ') # prints in line, not column

# help (range)

# word = 'python'
# for i in word:
#     print(i)
# data = [53, 76, 25, 98, 56, 42, 69, 81]
# total = sum(data) #function in Python
# total = 0
# for num in data:
#     total = total + num
# print(total)

# data = [53, 76, 25, 98, 56, 42, 69, 81]
# print('Max value',max(data))#function in Python
# # find_max = 0
# # for num in data:
# #     if num > find_max:
# #         find_max = num
# # print(find_max)

# my_list = [1, 11, 21, 31, 41, 51]
# for i in range(5):
#     print(my_list[i])
#     print(my_list[i + 1])
#     print()

# data = [53, 76, 25, 98, 56, 42, 69, 81]
# data_copy = data[:]
# print(data_copy)
# for i in range(len(data_copy)):
#     for j in range(0, len(data_copy) - i - 1):
#         if data_copy[j] > data_copy[j + 1]:
#             data_copy[j], data_copy[j + 1] = data_copy[j + 1],data_copy[j]
# print(data_copy)

# print(data_copy)
# print(sorted(data_copy))

# my_list = [34, 76, 58]
# # print(my_list)
# my_list.append(100)
# # print(my_list)
# # my_list.remove(34)
# # print(my_list)
# my_list.extend([67,68,69])
# print(my_list)
# my_list.pop(-1)
# print(my_list)
# #print(my_list.index(68))
# print(my_list)

# n = 10
# while n > 0:
#     print(n)
#     n = n - 1

# count = 0
# class_names = []
# name = input('Pl enter name. Type n to stop:> ')
# while name != 'n':
#     count += 1
#     class_names.append(name)
#     print(f'{name} has been added. ')
#     name = input('Next name?:> ')
# print(f'There are {count} people in the class, they are {class_names}')

# n = 100
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0: #important to have that condition in the beginig
#         print(i, 'Fizzbuzz!!!')
#     elif i % 5 == 0:
#         print(i, 'Buzz!')
#     elif i % 3 == 0:
#         print(i, 'Fizz!')
#     else:
#         print(i)
#
# print(list(range(10)))
# print(list(range(0, 20, 4)))

# import this

#

# my_list = input('Enter a string ')
# print(my_list)
# my_list = list(my_list)
# print(list.reverse(my_list))

# num_1 = int(input('Enter a number from 0 to 100: ' ))
# num_2 = int(input('Enter a number from 0 to 100: ' ))
# count = 0
# if num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print('Enter valid numbers.')
# else:
#     for i in range(num_1, num_2 +1):
#         print(i)
#         count = count + 1
#         print(count)
# print(count)

## count numbers in the range
# num_1 = int(input('Enter a number from 0 to 100: ' ))
# num_2 = int(input('Enter a number from 0 to 100: ' ))
# while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print('Enter valid numbers.')
#     num_1 = int(input('Enter a number from 0 to 100: '))
#     num_2 = int(input('Enter a number from 0 to 100: '))
#
# if num_1 < num_2:
#     for i in range(num_1, num_2+1):
#         print(i,end=' ')
# else:
#     for i in range(num_2, num_1+1):
#         print(i,end=' ')


## reverse string long way
# word = input('Enter a word: ')
# reverse_string = ''
# for char in word:
#     #print(char)
#     #reverse_string = char + reverse_string
#     reverse_string = reverse_string + char
#     print(reverse_string)
# print(reverse_string)

## reverse string short way
# word = input('Enter a word: ')
# print(word[::-1])

## times table
# a = int(input('Enter the number between 1 and 12: '))
# for i in range(1, 13):
#     #print(a, '*', i, '=', a*i)
#     print(f'{i} x {a} = {i*a}')

# user_input = input('Enter the number between 1 and 12: ')
# while (not user_input.isdigit() or (int(user_input)) < 1 or int(user_input) > 12):
#     print('Must be an integer between 1 and 12')
#     user_input = input('Enter the number between 1 and 12: ')
# user_input = int(user_input)
# print('====================')
# print()
# print(f'This is the {user_input} times table')
# print()
# for i in range(1, 13):
#     print(f'{i} * {user_input} = {i*user_input}')

# for i in range(1, 13):
#     print('=================')
#     print()
#     print(f'This is the {i} times table')
#     print()
#     for c in range(1, 13):
#         print(i, '*', c, '=', i*c)

## mean
# numbers = []
# s = 0
# n = 0
# for i in range(1, 5):
#     user_input = int(input('Please enter a number: '))
#     s = s + user_input
#     n = n + 1
#     numbers.append(user_input)
# print(numbers)
# print(s)
# print(n)
# print(len(numbers))
# print(s/len(numbers))

## factorial
# f = 1
# for i in range(1, 8):
#     f = f * i
#     print(f)
#     print(i)
# print(f)

# n = 15
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)

## Fibonnaci numbers
# fib = 0
# my_list = []
# for i in range(0, 20):
#     fib = i + fib
#     my_list.append(fib)
# print(my_list)
# print(fib)

# n = 20
# a = 0
# b = 1
# fib_num = []
# for i in range(n):
#     fib_num.append(a)
#     a,b = b,a+b
#     #a = b
#     #b = a + b
# print(f'The first  {n} Fibonnaci numbers are: {fib_num}')

## draw capital F letter
# star = '*'
# for i in range(1, 7):
#     for j in range(1, 6):
#         if i == 1 and j < 6:
#             print(star, end='')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j < 5:
#             print(star, end='')
#         elif i == 4 and j == 1:
#             print()
#             print(star)
#         elif i == 5 and j == 1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)

## Create list of odd and even numbers
# odd_list = []
# even_list = []
# for i in range(1, 101, 2):
#     odd_list.append(i)
# for j in range(2, 101, 2):
#     even_list.append(j)
# print(odd_list)
# print(even_list)

# n = 100
# evens = []
# odds = []
# for i in range(n + 1):
#     if not i % 2:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(f'The evens are {evens}')
# print(f'The odds are {odds}')

# import math
# print(math.pi)

# import random
# for i in range(100):
#     print(random.randint(1, 100), end='')

# import webbrowser
# webbrowser.open('https://docs.python.org/3/library/index.html')

capitals = {'Germany': 'Berlin', 'Spain': 'Madrid'}
print(capitals['Germany'])
