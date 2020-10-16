phrase = "Don't panick!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

for i in range(5):
    plist.pop()
plist.pop(0)
print(plist)
a = plist.pop()
b = plist.pop()
plist.extend([a, b])
plist.remove("'")
space = plist.pop(3)
plist.insert(2, space)
print(plist)
new_phrase = ''.join(plist)
print(new_phrase)