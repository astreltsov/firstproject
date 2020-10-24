usernames = ['oleg', 'admin', 'bruce', 'paganini']
for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a stat report?')
    else:
        print(f"Hello {username}, thank you for logging in again")