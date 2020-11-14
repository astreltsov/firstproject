def make_car(mfg, model, **car_info):
    """Build a dictionary containing everything we know about the car"""
    car_info['mfg_name'] = mfg
    car_info['model_name'] = model
    return car_info

car = make_car('Lada', 'Five',
               color = 'Yello',
               type = 'FWD')
print(car)