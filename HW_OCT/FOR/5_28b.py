import math
a = int(input('Enter the number less than 15: '))
nums = []
for num in range(a , 16):
    nums.append(num)
print(math.prod(nums))