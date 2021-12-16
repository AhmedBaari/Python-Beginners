'''
They help us make our programs more organized and powerful
 we deal with different types of data in python
 Not all info/data/things can be represented by strings booleans or numbers

 With classes we form our own data types.

 Consider you model a student. And it cannot be represented as a string
 '''

class student:
    def __init__(self, name, major, gpa, elite):
       self.name = name
       self.major = major
       self.gpa = gpa
       self.elite = elite

    def honor_roll(self):
      if self.gpa >= 3.5:
           return True
      else:
          return False

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
