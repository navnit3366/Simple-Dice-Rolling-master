import random
roll_again = True
min = 1
max = 6

while roll_again:
    rolled_num = random.randint(min,max)
    print("The dice rolled and you got: ", rolled_num)
    roll = input("Do you want to roll again?")
    if roll == "no":
        roll_again = False
