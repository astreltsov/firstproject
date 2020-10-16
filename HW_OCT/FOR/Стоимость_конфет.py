a = int(input('Цена 1 кг конфет '))
i = 0
b = 1
for i in range(0, 10):
    i = i + 1
    b = i*a
    print('Стоимость ', i, 'кг конфет', b)