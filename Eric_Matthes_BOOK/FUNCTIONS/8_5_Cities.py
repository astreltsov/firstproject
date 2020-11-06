# name = input("Please enter a city:> ")
# country = input("\nPlease enter country:> ")
# def describe_city(city, country):
#     print(f"\n{city.title()} is in {country.title()}")
# describe_city(city, country)

def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')