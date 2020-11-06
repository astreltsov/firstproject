pets = []
pet1 = {
    'type': 'cat',
    'name': 'silly',
    'age': 2,
    }
pet2 = {
    'type': 'dog',
    'name': 'stel',
    'age': 5,
    }
pet3 = {
    'type': 'bird',
    'name': 'fifa',
    'age': 25,
    }
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    t = pet['type'].title()
    n = pet['name'].title()
    a = str(pet['age'])
    print(t + " by the name " + n + " is " + a + " years old.")

