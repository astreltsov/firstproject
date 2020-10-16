a = int(input('Ввести начальное число '))
b = int(input('Ввести конечное число '))
# i = b
d = 0
for i in range(a, b - 1 , -1):# start = 10, end = -1, step = -1
    print(i)
    d = d + 1
print('Количество чисел ', d)