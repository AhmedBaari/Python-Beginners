#exponent
print(2**3)

#How to use a for loop to create a function like this on our own
def exp(base, pwr):
    result = 1
    for i in range(pwr):
        result = result * base
    return result

print(exp(3,4))