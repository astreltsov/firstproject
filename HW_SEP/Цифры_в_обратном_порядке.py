a = int(input('Ввести число: '))
result = ""
while a > 0:
    n = a % 10
    a = a // 10
    result = result + str(n)  # result += str(n)
result = int(result)
print(result)
print(type(result))
