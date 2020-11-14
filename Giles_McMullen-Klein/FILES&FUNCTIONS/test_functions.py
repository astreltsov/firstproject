# def hello():
#     print('Hello, world!')
# for i in range(5):
#     hello()

# def hi(name):
#     print(f"Hello, {name}!")
# for i in range(5):
#     hi('Oleg')

# def hi(name = 'Oleg'):
#     print(f"Hello, {name}!")
# hi('Mary')

# n=20
# a = 0
# b = 1
# for i in range(n):
#     a,b = b,a+b
# print(a)

# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a,b = b,a+b
#     return a
# fib_num = fib(20)
# print(fib_num)
# for i in range(20):
#     print(fib(i))

# def calc_mean(first, *remainder):
#     mean = (first + sum(remainder))/(1 + len(remainder))
#     print(type(remainder))
#     return mean
# print(calc_mean(23, 43, 56, 76, 45, 100, 95))

# a = tuple('Hello world')
# print(a)

# def fib_2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_2(n-1) + fib_2(n-2)

# x = fib_2(20)
# print(x)
#
# y = fib(36)
# print(y)

## not working
# import timeit
# t1 = timeit.Timer("fib(36)")
# print(t1.timeit(5))

# def sum_and_mult(a,b):
#     total = a + b
#     product = a * b
#     return total, product

# func_call = sum_and_mult(3, 4)
# print(func_call)
# print(type(func_call))

# v1, v2 = sum_and_mult(6, 7)
# print(v1)
# print(v2)

# def lengthen_list(n, my_list = [1, 2, 3]):
#     my_list.append(n)
#     return my_list
# x = lengthen_list(4)
# print(x)
# x = lengthen_list(4)
# print(x)

def lengthen_list(n, my_list = None):
    if my_list == None:
        my_list = [1, 2, 3]
        my_list.append(n)
        return my_list

x = lengthen_list(4)
print(x)
x = lengthen_list(4)
print(x)