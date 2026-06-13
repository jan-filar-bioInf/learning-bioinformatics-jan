#asking for the level n
#import random module to generate random number
import random

#ask for positiv level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
             break
    except ValueError:
        pass
# generate a positiv number between 1 and to choosen level
number = random.randint(1,level)

#keep asking user for number until correct number guessed 
while True:
    try:
        userguess = int(input("Guess: "))
        if userguess <= 0 :
            continue
        if userguess < number :
            print ("Too small!")
        elif userguess > number :
            print ("Too large!")
        else:
            print ("Just right!")
            break

    except ValueError:
        pass



