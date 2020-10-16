d = int(input('Введите число '))
a = int(input('Введите цифру '))
s = 0
#d = 123 -> 12

# подсчет суммы всех цифр числа
# while d > 0:
#     last_digit = d % 10
#     s = s + last_digit
#     d = d // 10
# print(s)





while d > 0:
    last_digit = d % 10
    if last_digit == a:
        s = s + 1
    d = d // 10
print(s)





# n1 = d % 10
# #n1 = int(n1)
# if n1 = a
#     s = (s + 1)
# n2 = (d // 10) % 10 #if n2 = x: s = s + 1
# n3 = d // 100 #if n3 = x: s = s + 1
# print(n1, n2, n3)
# print(s)

#l = str(d)
#b = len(l)
#print(b)
#i = 0
#while(i < b):

#a = 0
#s = 0
#for i in range(a , b)
#n1 = d % 10 if n1 = x: s = s + 1
#d = d // 10
#n2 = d % 10 if n2 = x: s = s + 1
#d = d // 10
#n3 = d % 10 if n3 = x: s = s + 1
#print(n1, n2, n3)
#print(s)