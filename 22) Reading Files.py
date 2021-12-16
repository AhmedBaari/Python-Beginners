

Employee_Data = open("Employees.txt", "r")

print(Employee_Data.readable()) #Is the file readable?
print(Employee_Data.read()) #read the entire file
print(Employee_Data.readline()) #Reads the first line and moves cursor to beginning of next line
#print(Employee_Data.readlines()[1]) #SOMETHING IS WRONG
Employee_Data.close() #make sure to close it

Employee_Data = open("Employees.txt", "r")
for employee in Employee_Data.readlines():
    print(employee)
Employee_Data.close()