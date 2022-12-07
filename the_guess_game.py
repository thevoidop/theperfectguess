import random

randNum = random.randint(1,100)
print("\t\tComputer is choosing a random number\n")
gusses = 0
userInput = None

while (True):
        while(userInput != randNum):
            try:
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
            except Exception as e:
                 print("Please enter a valid number")
        break
    
#with open("game_hs.txt") as f:
#    record = int(f.read())
#if (gusses < record):
#    with open("game_hs.txt", "w") as f:
#        f.write(str(gusses)) 
