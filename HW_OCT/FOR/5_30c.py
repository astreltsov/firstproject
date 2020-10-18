import math
n = int(input('Enter the number less than 100: '))
nums = []
for num in range(1 , n + 1):
    nums.append(pow(num, 2))
print(sum(nums))