import random 
num= random.randint(1,9)
chance=5
print("number guessing game!")
while chance>0:
    guess=int(input("Enter your guess"))
    if guess ==num:
        chance=0
        print("congratulations, you won!")
    elif guess>num:
        chance=chance-1
        print("try lower")
    elif guess<num:
        chance=chance-1
        print("try higher")