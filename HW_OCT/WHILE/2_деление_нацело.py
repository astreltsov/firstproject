N = int(input('Введите число '))
i = 1
R = 0
result = ""
while i <= N:
    R = (N % 10)
    result = result + str(R)  # print(R)
    i = i + 1
result = int(result)
print(result)
