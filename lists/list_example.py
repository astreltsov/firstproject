from datetime import datetime

#import time
#from time import sleep
import random
import time

# def sleep(time_for_wait):
#     print("z-z-z-z", time_for_wait)


odds = [1, 3, 5, 7, 9, 11, 59]

right_this_minute = datetime.today().minute
print(right_this_minute)


for i in range(5):# range(start, end, step) range(10, 0, -1)
    if right_this_minute in odds:
        print("'минута нечетная")
    else:
        print("минута четная")
    wait_time = random.randint(1,60)
    print(wait_time)
    time.sleep(wait_time)



# for i in [1, 2, 3]:
#     print(i)
#
# for ch in "Hi!":
#     print(ch)

