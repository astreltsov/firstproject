a = int(input('Введите число '))
i = 2
is_two_exist = False
while a > 0:
    b = a % 10
    if b == 2:
        is_two_exist = True
        break
    a = a // 10

if is_two_exist:
    print('TRUE')
else:
    print('FALSE')

#wait_time = random.randint(1,60)
#word = 'bottels'