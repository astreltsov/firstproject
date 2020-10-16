a = int(input('Веедите число '))
c = int(input('До какого множителя вы хотите дойти '))
i = 0
while i <= c:
    b = a * i
    print(a, '*', i, '=', b)
    i = i + 1

# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print(a)