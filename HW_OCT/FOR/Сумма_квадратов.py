a = int(input('Введите начальное число '))
b = int(input('Введите конечное число '))
i = 0
c = a ** 2
for i in range(a , b):
    i = i + 1
    c = c + (i ** 2)
print(c)
