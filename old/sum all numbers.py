a = int(input("a="))#4
s = 0
while a > 0:
    s += a % 10# s = s % 10
    a //= 10# a = a //10
print("s=", s)
