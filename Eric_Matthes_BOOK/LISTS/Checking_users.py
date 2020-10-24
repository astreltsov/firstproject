current_users = ['OLEG', 'admin', 'bruce', 'paganini', 'wallace']
new_users = ['bill', 'peter', 'oleg']
current_user_l = []
for user in current_users:
    current_user_l.append(user.lower())
print(current_user_l)

# for new_user in new_users:
#     if new_user in current_users:
#         print(f"Welcome {new_user.title()}!")
#     else:
#         print(f"{new_user.title()} needs to be added.")
