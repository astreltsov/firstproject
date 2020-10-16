N = int(input('Введите число '))
s = 0
i = 0
while N > 0:
    s = s + N % 10
    N = N // 10
    i = i + 1
print('Сумма чисел ', s, 'Кол-во числе', i)
