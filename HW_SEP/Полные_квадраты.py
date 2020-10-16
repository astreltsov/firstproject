import math

a = int(input('Введите начальное число '))
b = int(input('Введите конечное число '))
for i in range(a, b + 1):
    s = math.sqrt(i)
    if int(s) == s: print(s)
