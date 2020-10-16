import random

secret = random.randint(1,999)
guess = 0
tries = 0

print ("-----(1-999)")

while guess != secret and tries < 10:
    guess = int(input ("your guess "))
    if guess < secret:
        print("too small")
    elif guess > secret:
        print("too much")
    tries = tries + 1
if guess == secret:
    print ("you are right")
else:
    print ("you lost. the right number is", secret)
