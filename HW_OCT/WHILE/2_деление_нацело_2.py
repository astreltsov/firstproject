N = int(input('Введите число '))
while N > 0:
    digit = N % 10
    print(digit)
    #123->12 //
    N = N // 10

