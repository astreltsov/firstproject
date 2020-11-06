# my_list_1 = [1, 2, 3, 4]
# my_list_2 = ['a', 'b', 'c', 'd', 'e']
#
# joined = list(zip(my_list_1, my_list_2))
# print(joined)
#
# i, j = zip(*joined)
# print(i)
# print(j)
# import random
# for i in range(100):
#     print(random.randint(1,100), end=' ')
#print(random.randint(1,99))

# import webbrowser
# webbrowser.open('https://docs.python.org/3/')

## Count each letter in a text
# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# letter_count = {}
# for letter in sherlock:
#     letter_count[letter.lower()] = letter_count.get(letter,0) + 1
#     #print(letter_count)
# #letter_count['m'] = 1
# #print(letter_count)
# letter_count_clean = {}
# for k, v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k] = v
#     print(k, v)
#print(letter_count_clean)

# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# new_words = sherlock.split(' ')
# print(new_words)
# for i in range(len(new_words)):
#     new_words[i] = new_words[i].strip('y')
# print(new_words)
# print('Bohemia' in new_words)

# my_tuple = [1, 2, 3, 4]
# print(my_tuple[:3])

# my_list = [[1, 2, 3], [4,5,6], [7,8,9]]
# print(my_list[1][1])

# countries = {
#     'France': {
#         'Capital': 'Paris',
#         'Language': 'French'},
#     'Spain': {
#         'Capital': 'Madrid',
#         'Language': 'Spanish'},
#     'UK': {
#         'Capital': 'London',
#         'Language': 'English'},
#     }
# #print(countries['France'])
# for k, v in countries.items():
#     print(f"{v['Capital']} is the capital of {k}, they speak {v['Language']}.")

# sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
# letter_count = {}
# for letter in sherlock:
#     letter_count[letter.lower()] = letter_count.get(letter,0) + 1
# letter_count_clean = {}
# for k, v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k] = v
# from collections import Counter
# new_dict = dict(Counter(sherlock.lower()))
# new_dict = {k:v for k, v in new_dict.items() if k.isalpha()}
# print(new_dict)

# l = [x**2 for x in range(1, 11)]
# print(l)

sherlock = 'A scandal in Bohemia The Red-headed League A case of identity The Boscombe Valley mystery The five orange pips The man with the twisted lip The adventure of the blue carbuncle The adventure of the speckled band'
letter_count = {}
for letter in sherlock:
    letter_count[letter.lower()] = letter_count.get(letter,0) + 1
letter_count_clean = {}
for k, v in letter_count.items():
    if k.isalpha():
        letter_count_clean[k] = v
    print(k, v)