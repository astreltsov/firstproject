a = int(input('Цена 1 кг конфет '))
i = 0
b = 1 # вес
c = 1 # стоимость
for i in range(0, 10):
    i = i + 1
    b = i * 0.1
    c = b * a
    print('Стоимость ', b, 'кг конфет', c)

