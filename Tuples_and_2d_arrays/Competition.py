n = int(input('Enter the number of athlets: '))
m = int(input('Enter the number of throws: '))
arr = []
for i in range(n):# игроки
    arr_ath = []
    print("athlete", i)
    for j in range(m):# броски
        x = int(input("throw="))
        arr_ath.append(x)
    arr.append(arr_ath)
print(arr)

for i in range(n):#row
    for j in range(m):#column
        print(arr[i][j], end = " ") # replace enter with space
    print()

max_sum = 0
s = 0
idx_max = 0
for i in range(n):#row
    s = 0
    for j in range(m):#column
        s += arr[i][j]
    if s > max_sum:
        max_sum = s
        idx_max = i
print(max_sum, idx_max)
# 00 01
# 10 11
s = 0
s_max = 0
for person in arr:
    s = sum(person)
    if s > s_max:
        s_max = s
print(s_max)
# 2
# 2
# 5
# 4
