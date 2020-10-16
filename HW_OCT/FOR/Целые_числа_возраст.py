a = int(input('Введите начальное число '))
b = int(input('Введите конечное число '))
c = 1
for i in range(a, b + 1):
    print(i)
    # i = i + 1
    c = c + 1
print('Количество чисел ', (c - 1))