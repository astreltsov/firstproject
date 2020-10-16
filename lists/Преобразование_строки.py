phrase = "Don't panic!"
plist = list(phrase)# превращает строку в список
print(phrase)
print(plist)
for i in range(4):
    plist.pop()#delete last elem
plist.pop(0)
a = plist.pop()
p = plist.pop()
plist.extend([a, p])
plist.remove("'")
space = plist.pop(3)
plist.insert(2, space)
print(plist)

new_phrase = "".join(plist) #превращает список в строку
print(new_phrase)