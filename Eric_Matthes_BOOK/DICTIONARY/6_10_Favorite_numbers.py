favorite_numbers = {
    'oleg': [25, 5, 8],
    'natali': [99,33, 45],
    'peter': [7, 14, 21],
    'vicky': [8, 24, 48],
    }
for user, nums in favorite_numbers.items():
    print(f"{user.title()}'s favorite numbers are: ")
    for num in nums:
        print(num)