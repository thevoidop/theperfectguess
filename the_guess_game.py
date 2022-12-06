import random

randNum = random.randint(1,100)
print("\t\tComputer is choosing a random number\n")
gusses = 0
userInput = None

while(userInput != randNum):
    userInput = int(input("Guess the number: "))
    gusses += 1
    if (userInput == randNum):
        print("\nCongratulations! You guessed it right.")
        print(f"It took you {gusses} gusses to win.")
    else :
        if (userInput < randNum):
            print("You gussed it wrong! Choose a HIGHER numer.\n")
        else :
            print("You gussed it wrong! Choose a LOWER numer.\n")
    
with open("game_hs.txt") as f:
    record = int(f.read())
if (gusses < record):
    with open("game_hs.txt", "w") as f:
        f.write(str(gusses)) 
    