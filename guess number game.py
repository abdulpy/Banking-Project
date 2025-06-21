import random

target=random.randint(1,100)

while True:
    userchoice=int(input("Guess the Number: "))
    if(userchoice==target):
        print("Succeed")
        break
    elif(userchoice<target):
        print("Number is small")
        # print("My Gussing number is: ",target)
    else:
        print("Number is Big")

print("Game Ended")