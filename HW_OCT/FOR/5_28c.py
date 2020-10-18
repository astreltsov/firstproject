import math
b = int(input('Enter the number more than 1: '))
nums = []
for num in range(1 , b + 1):
    nums.append(num)
print(math.prod(nums))