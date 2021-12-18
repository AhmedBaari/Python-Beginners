'''
STRINGS
"Strings are arrays of bytes representing Unicode characters" 
Use single, double or triple quotes to show a string.
'''

#Variables in a python program gives data to the computer for processing
character_name = "Berry" #This is a string variable
character_age = "17.5678213" #no need quotation mark for number
is_Male = True #Boolean Variable

#EXAMPLE STORY    👇String              👇Variable      👇String      
print("There once was a man named " + character_name + ", ") #This print statement has both strings and variables joined with concatenation operator (+)
print("He was " + character_age +  " years old.")   

#String Variable
character_name = "Tba"
character_age = "15"
print("He really liked the name " + character_name + ", ")
print("But didn't like being " + character_age +  ".")

'''OUTPUT
There once was a man named Berry,He was 17.5678213 years old.
He really liked the name Tba,
But didn't like being 15.
'''