# f = open('kipling.txt', 'w')
# print(type(f))
# f.write('If you can keep your head while all about  you \nare losing theirs and blaming it on you, \n')
# f.close()

# f = open('kipling.txt', 'r')
# print(type(f))
# print(f.read())
# f.close()

# f = open('kipling.txt', 'a')
# f.write('If you can dream - and not make dreams your master;\n\
# if you can think - and not make thoughts your aim;\n')
# f.close()
# print()
# f = open('kipling.txt', 'r')
# print(f.read())
# f.close()
# print()

with open('kipling.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')