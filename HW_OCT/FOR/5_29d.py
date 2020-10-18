import statistics
a = int(input('Enter the number: '))
b = int(input('Enter the number more than b: '))
nums = []
for num in range(a, b + 1):
    nums.append(num)
print(statistics.mean(nums))