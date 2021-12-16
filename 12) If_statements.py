is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are male but not tall")
else:
    print("You are either not male or not tall or both")

#--- COMPARISONS
def max_num(a,b,c): # != means not equal to
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(max_num(a,b,c))