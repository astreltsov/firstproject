import math
a = int(input('Enter the number less than 50: '))
nums = []
for num in range(a , 51):
    nums.append(pow(num, 2))
print(sum(nums))