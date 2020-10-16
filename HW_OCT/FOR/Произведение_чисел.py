a = int(input('Ведите начальное число '))
b = int(input('Ведите конечное число '))
p = 1
for i in range(a , b + 1): #[0, 1, 2, 3...10]
    # i = i + 1
    p = p * i
print(p)