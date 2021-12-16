#define
def say_hi():
    print("Hello User")

print("top") #comes 1st
say_hi() #calling say hi, comes 2nd
print("bottom") #comes 3rd

def heya(name, age):
    print("Hello " + name + "! You are " + age + " years old.")

name = input("Your name: ")
age = input("Your age: ")
heya(name, age)