p = int(input('Введите цену 1 кг сыра: '))
for i in range(50, 1000, 50):
    print('Цена ', i, 'грамм сыра = ', p / 1000 * i)