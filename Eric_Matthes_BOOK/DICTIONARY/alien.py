# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# #print(alien_0['points'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# print(alien_0['points'])

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(f"The alien is now {alien_0['color']}")
#
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0 = {}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'fast'
# print(f"Original position: {alien_0['x_position']}")
# # Move alien to the right
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# # The new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# print(alien_0)

alien_0 ={'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)