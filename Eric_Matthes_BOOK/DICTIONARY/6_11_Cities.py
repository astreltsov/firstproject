cities = {
    'moscow': {
        'country': 'russia',
        'population': '15 mln',
        'fact': 'many churches',
    },
    'new your': {
        'country': 'usa',
        'population': '8.3 mln',
        'fact': 'many cultures',
    },
    'paris': {
        'country': 'france',
        'population': '2.1 mln',
        'fact': 'good food'
    }
}
for city, fact in cities.items():
    print(f"Information about {city.title()}: ")
    print(f"\t{fact['country']}")
    print(f"\t{fact['population']}")
    print(f"\t{fact['fact']}")