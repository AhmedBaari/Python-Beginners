#First create 3 variables
a = float(input("Enter first number: "))
o = input("Enter operator: ")
b = float(input("Enter third number: "))


if o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "/":
    print(a/b)
elif o == "*":
    print(a*b)
else:
    print("Invalid Operator")