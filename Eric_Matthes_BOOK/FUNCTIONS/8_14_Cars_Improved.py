def make_car(mfg, model, **car_info):
    """Build a dictionary containing everything we know about the car"""
    car_dict = {
        'mfg': mfg.title(),
        'model': model.title(),
    }
    for option, value in car_info.items():
        car_dict[option] = value

    return car_dict

my_lada = make_car('Lada', 'Five',
               color = 'Yello',
               tow_package=True,
                   type = 'FWD')
print(my_lada)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)