#10 3
s = input().split()# #['10', '3'] метод строки - разбивает строку по разделителю (пробел)
a = int(s[0])
b = int(s[1])
print(a, b)
ls = []#create empty list
for i in range(a):#fill list "I"
     ls.append('I')
print(ls)

#проход по броскам
for i in range(b):
    borders = input().split() #['8', '10']
    l = int(borders[0])#"8" -> 8 превращаем строку "8" в число 8 (str->int)
    r = int(borders[1])
    for i in range(l, r + 1):
        ls[i-1] = "." # i-> "."
    print(ls)