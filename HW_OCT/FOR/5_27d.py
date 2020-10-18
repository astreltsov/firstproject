a = int(input('Enter the number: '))
b = int(input('Enter the number, higher than a: '))
nums = []
for num in range(a , b+1):
    nums.append(num)
print(sum(nums))