# import random
from random import randint

N = int(input("N:"))
s = 0
for i in range(N):
    #a = int(input('Введите число '))
    a = randint(5, 10)
    print(a)
    s = s + a
print(s)

