favorite_places = {
    'oleg': ['crete', 'santa cruz', 'snegiri'],
    'anna': ['zug', 'miami', 'samara'],
    'nick': ['spb', 'kiev', 'varshava']
}
for name, locations in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for location in locations:
        print(f"\t{location}")
