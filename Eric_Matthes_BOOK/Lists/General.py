# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     #print(magician)
#     print(f"{magician.title()}, that was a great trick!")

# numbers = list(range(1, 6))
# print(numbers)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = [value**2 for value in range(1, 11)]
# print(squares)

players = ['charly', 'martina', 'michael', 'florence', 'eli']
print(players)
#print(players[2:])
#print(players[-3:])
for player in players[:3]:
    print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_foods[:]
# my_foods.append('cannoli')
# friend_food.append('ice cream')
# print(my_foods)
# print('The last two items in friend_food are:', friend_food[-2:])
# for food in my_foods[-2:]:
#     print(food)