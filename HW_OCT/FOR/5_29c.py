import statistics
a = int(input('Enter the number less than 200: '))
nums = []
for num in range(a, 201):
    nums.append(num)
print(statistics.mean(nums))