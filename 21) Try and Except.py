


#try except tries to run a code and if something goes wrong, it uses the catch code.

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: 
    print(err)
except TypeError: 
    print("Something's wrong with the code")
except ValueError: 
    print("Invalid Input")