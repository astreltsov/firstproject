N = int(input('Увеличение длинны пробега (%) '))
S = 10
P = 10
i = 1
while P < 200:
    S = S * (1 + N / 100)
    i = i + 1
    P = P + S
    #print(i , S , P)
print('Суммарный пробег лыжника превысит 200 км через ', i , 'дней и составит ', int(P), 'км')
