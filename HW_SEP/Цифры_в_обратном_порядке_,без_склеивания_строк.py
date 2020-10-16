a = int(input('Ввести число:'))
amount = 0
temp_a = a
while temp_a > 0:
    n = temp_a % 10
    temp_a = temp_a // 10
    amount += 1


amount = amount - 1
r = 0
while a > 0:
    n = a % 10
    r += n * (10**amount)
    a = a // 10
    amount -= 1
print(r)
