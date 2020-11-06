## list of dictionaries
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

aleins = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aleins.append(new_alien)
for alein in aleins[:5]:
    print(alein)
print("...")
print(f"Total number of aliens: {len(aleins)}")

for alein in aleins[:3]:
    if alein['color'] == 'green':
        alein['color'] = 'yellow'
        alein['speed'] = 'medium'
        alein['points'] = 10
for alein in aleins[:5]:
    print(alein)
print("...")