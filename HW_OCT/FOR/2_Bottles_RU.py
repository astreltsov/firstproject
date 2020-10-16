word = 'бутылки'
for beer_num in range(19, 0, -1):
    print(beer_num, word, 'пивных бутылок на столе.')
    print(beer_num, word, 'пива.')
    print('возьми одну.')
    print('передай её.')
    if beer_num == 1:
        print('Не осталось больше пивных бутылок на столе.')
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = 'бутылка'
        print(new_num, word, "пивных бутылок на столе.")
    print()