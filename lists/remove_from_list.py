nums = [1, 2, 3, 4]
print(nums)
# nums.remove(3)
removed_elem = nums.pop(0)
#removed_elem = nums.pop() - remove last elem
print(removed_elem)
print(nums)
nums.extend([33,44])
nums.insert(2, 77)
print(nums)

for i in range(len(nums)):
    print("i=", i, "elem=", nums[i])

for elem in nums:
    print(elem)