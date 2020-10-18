import statistics
b = int(input('Enter the number more than 150: '))
nums = []
for num in range(150 , b + 1):
    nums.append(num)
print(statistics.mean(nums))