a = int(input('Введите число '))
b = 0
for i in range(1, a + 1): #a = 5 , [0, 1, 2, 3, 4]
    if a % i == 0: #если делится без остатка
        b = b + 1
        print(i)
print(b)