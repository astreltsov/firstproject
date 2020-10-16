a = int(input('Введите число '))
for i in range(1, a + 1): #a = 5 , [0, 1, 2, 3, 4]
    if a % i == 0: #если делится без остатка
        print(i, end =" ")


