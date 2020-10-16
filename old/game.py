import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print("-----(1-99)")

while guess != secret and tries < 6:
    guess = int(input("твой вариант?"))
    if guess < secret:
        print("Это слишком мало")
    elif guess > secret:
        print ("Это слишком много")
    tries = tries + 1 #2
if guess == secret:
    print('win')
else:
    print('you lost. the right number is', secret)
    
