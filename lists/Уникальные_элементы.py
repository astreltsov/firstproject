plist = input("list=").split()
print(plist)
for i in range(len(plist)):
    plist[i] = int(plist[i])
print(plist)
new_plist = []

for i in range(len(plist)):
    new_plist.append(0)

for i in range(len(plist)):
    elem = plist[i]
    new_plist[elem - 1] = new_plist[elem - 1] + 1
for i in range(len(plist)):
    if plist[i] == 1:
        print("r=", i+1)
print(new_plist)
