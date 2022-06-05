import random
chance = 10
loop = 1
win_count = 0


print("Rolling dice...")
print("Getting result...")
for loop in range(chance):
    roll = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    if roll == roll2:
        print("You Win!!...your values are:", roll, roll2)
        win_count = win_count + 1
        print("Your winning rate was:", ((roll+roll2)/12)*100, "%")
    else:
        print("Better luck next time!!...your rolls were:", roll, roll2)
        print("Your winning rate was:", ((roll+roll2)/12)*100, "%")
win_rate = 0
print("You have exhausted your chances..")




