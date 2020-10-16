a = int(input('Введите число '))
r = ''
while a > 0:
    n = a % 10
    a = a // 10
    r = r + str(n)
r = int(r)
print(r)