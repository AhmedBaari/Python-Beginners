'''
NUMBERS
In python, several functions can be used for various calculations, thus making life easier :)
'''

# These are numbers not strings, so we won't enclose them in quotations
print(3 / 5 + 5) #5.6
print((3 / 4) + 5) #5.75
print(10 % 3) #1 # 10/3 is 3 with remainder 1. Mod gives remainder 1

my_num = 5 #Assiging an integer to a variable
print(my_num) #5
print(str(my_num) + " is my favourite number") #5 is my favourite number #Numbers cannot be concatenated with strings. We have to convert number to string before joining with another string in Print() command

#Common Functions
print(pow(4,6)) #4096 #3^2
print(max(4,6)) #6 #which number is higher
print(min(4,6)) #4 #which number is lower
print(round(3.7)) #4 #which number is higher

#Functions from Math Module
from math import * #For doing more math, we can import the math module
print(floor(3.7)) #4 #Rounds to the nearest larger number
print(ceil(3.7)) #4 #Rounds to the nearest larger number
print(sqrt(36)) #6.0