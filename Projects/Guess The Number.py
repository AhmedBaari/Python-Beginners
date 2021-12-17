import random
import os

def rguess():
    random_number = random.randint(1,1000)
    return random_number

random_number=rguess()
guess = None
tries = 0

while guess != random_number:
  print("No. of attempts done: ", tries)
  guess = int(input("Guess a number between 1 and 1000: "))
  tries += 1
  z = guess - random_number
  os.system("clear") #For clearing the console
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
#print("nice", end='')  #for clearing the console
print("You Did It!!! The correct answer is ", random_number) #This statement doesn't get printed idk how to not let it get cleared 

#After correct answer it goes back into the while loop which shouldn't happen.

# Improvements/Changes
# 1. Added a new module to clear the console since the initial code was quite gay.
# 2. made subtle imporvements to the code to further improve functionality
