'''
FUNCTIONS: ONE OF THE MOST IMPORTANT PARTS OF PYTHON
A Python function is a group of code that can be called from anywhere after it is defined. Functions can return a value using a return statement.
 Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ). Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
'''
#Defining a python
def say_hi():
    print("Hello User")
#It won't run until it is called using say_hi()

print("top") #Comes 1st
say_hi() #Hello User #Calling say_hi, comes 2nd
print("bottom") #Comes 3rd

def heya(name, age): # 2 variables used here
    print("Hello " + name + "! You are " + age + " years old.")

name = input("Your name: ") #First Variable
age = input("Your age: ") #Second Variable
heya(name, age) #Calling function using the 2 variables