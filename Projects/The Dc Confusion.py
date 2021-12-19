'''Dicionary allows us to store information in KEY, VALUE PAIRS. Keys should be unique
For example:
DC = {
    "Jan": "Janurary",
    "Feb": "February",
    "Mar": "March"
} 
In this, "Jan" is the key and "January" is the value.
print(DC["Feb"]) gets the value of the key "Feb"

1 is different from '1' because 1 is an integer, '1' is a string.
'''

dc1 = {}  # {} 
dc1[1]=1 #{1: 1} #Assigns Value 1 to key 1
dc1['1'] = 1 #{1: 1, '1': 1} #Assigns value 1 to key '1'
dc1['1']=2 #{1: 1, '1': 2} #Assigns value 2 to key '1'
dc1[1.0] = 4 #{1: 4, '1': 2} #Assigns value 4 to key '1

sum = 0 
for k in dc1: 
    sum += dc1[k] #2+4 #adding the keys
print(sum) #6