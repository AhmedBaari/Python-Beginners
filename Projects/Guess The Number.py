import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    tries = 0
    while guess != random_number:
        
        print("No. of attempts taken: " + str(tries))
        guess = int(input(f"Guess a number between 1 and {x}: "))
        tries += 1
        
        z = guess - random_number
        print("\033c\033[3J", end='') #For clearing the console
        if z > 500:
            print("Woah too high, try going much lower")
        elif z > 250:
            print("Quite high, try going more lower")
        elif z > 125:
            print("That's high, try going lower")
        elif z > 63:
            print("That's a bit high, try going lower")
        elif z > 30:
            print("Almost there, go lower")
        elif z > 15:
            print("Almost there, slowly go lower")
        elif z > 7:
            print("That's so close, decrease it a bit")
        elif z > 3:
            print("Super Close! Carefully decrease it")
        elif z < -500:
            print("Woah too low, try going much higher")
        elif z < -250:
            print("Quite low, try going more higher")
        elif z < -125:
            print("That's low, try going higher")
        elif z < -63:
            print("That's a bit low, try going higher")
        elif z < -30:
            print("Almost there, go higher")
        elif z < -15:
            print("Almost there, slowly go higher")
        elif z < -7:
            print("That's so close, increase it a bit")
        elif z < -3:
            print("Super Close! Carefully infc it") 
    print("\033c\033[3J", end='')  #for clearing the console
    print("You Did It!!! The correct answer is " + str(random_number)) #This statement doesn't get printed idk how to not let it get cleared 

    #After correct answer it goes back into the while loop which shouldn't happen.
    
guess(1000)