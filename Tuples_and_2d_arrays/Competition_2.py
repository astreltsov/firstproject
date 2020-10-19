n = int(input('Enter the number of athlets: '))
m = int(input('Enter the number of throws: '))
arr = []
for i in range(n):
    arr_ath = []
    print("number", i)
    for j in range(m):
        x = int(input("throw="))
        arr_ath.append(x)
    arr.append(arr_ath)
print(arr)

max_value = 0
current_max = 0
for i in range(n):# for row
    for j in range(m):#for column
        if arr[i][j] > current_max:
            current_max = arr[i][j]
    if current_max > max_value:  # [1, 2, 3]
        max_value = current_max
print(max_value)
