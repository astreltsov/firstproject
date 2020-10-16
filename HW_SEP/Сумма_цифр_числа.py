a = int(input('Введите трехзначное число '))
n1 = a % 10
n2 = (a // 10) % 10
n3 = a // 100
print(n1, n2, n3)
print(n1 + n2 + n3)