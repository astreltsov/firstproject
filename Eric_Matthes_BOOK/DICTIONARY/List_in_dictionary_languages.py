##List in dictionary
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'huskell']
}
for name, languages in favourite_languages.items():
    if len(languages) == 1:
        #print(f"\n{name.title()}'s favorite language is {languages}")
        s = " ".join(languages)
        print(f"\n{name.title()}'s favorite language is {s}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")