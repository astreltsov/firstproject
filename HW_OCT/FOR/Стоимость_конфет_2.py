a = int(input('Цена 1 кг конфет '))
i = 0
b = 0 # вес
c = 0 # стоимость
for i in range(11, 20, 2):
    i = i + 1
    b = i / 10
    c = b * a
    print('Стоимость ', b, 'кг конфет', c)
