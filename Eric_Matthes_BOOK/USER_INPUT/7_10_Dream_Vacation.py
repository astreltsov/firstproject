# prompt = "Where do you want to go? "
# prompt += "\nEnter quit to finish. "
# while True:
#     destination = input(prompt)
#     if destination != 'quit':
#         print(f"\nYour favourite destination is {destination}")
#     else:
#         break

name_prompt = "Enter your name: "
place_prompt = "\nEnter place "
repeat_prompt = "\nDo you have any other favourite places? (Yes/No)"

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    #store the results
    responses[name] = place
    #check for more answers
    repeat = input(repeat_prompt)
    if repeat != 'yes':
        break
#Show the results of the survey
print(f"\n ---- The results are: ---- ")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}")