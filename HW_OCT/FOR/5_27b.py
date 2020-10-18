n = int(input('Enter the number less than 400: '))
nums = []
for num in range(n, 401):
    nums.append(num)
print(sum(nums))