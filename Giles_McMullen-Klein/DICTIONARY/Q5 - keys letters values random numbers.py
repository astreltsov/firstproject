import random
k = 'ABCDEFGH'
d = {}
for letter in k:
    d[letter] = random.randint(1, 100)
print(d)