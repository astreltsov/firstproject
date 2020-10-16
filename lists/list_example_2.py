# prices = []
# temps = [32.0, 34.0]
# words = ["sdfsd", "dfsdf", 2, temps]
# print(words)
vowels = ['a', 'e', 'i', 'o', 'u']
found = []
# found.append('a')
# found.append('e')
# found.append('o')
# print(found)
# print("len=", len(found))
word = "Hello eee".lower()
#in
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
# print(found)
for v in found:
    print(v)