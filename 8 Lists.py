'''
LISTS
Lists are used to store multiple items in a single variable
'''

#Consider I make a list of my best friends
friends = ["Manish", "Siva", "Nagarjun", "Shravan", "Shakthi", "Siva", "Pritham", "Jarvis", "Srikanth", "Devadarshan", "Anjjai"]

#Now I want to know the list of my best friends
print(friends) #Prints the entire list

#I want to know who my 4th best friend is so I'll take "3" as index (cuz zero is counted)
print(friends[3]) #Siva

#I just got another best friend, I want to replace my 2nd best friend with her. We use list[index] for this
friends[1]= "Tayeba" #Assigns "Tayeba" to index[2] in the list
print (friends[1]) #Tayeba #(Just checking)

#I just got another new friend, let me add her to the end of the list. We use append() for this
friends.append("Salha")
#We can use list.insert[index] too for inserting a value without deleting anything else. It is simpler. Oh yes, Deetch is amazing!
friends.insert(1, "Deetchana") 
print(friends) #['Manish', 'Deetchana', 'Tayeba', 'Nagarjun', 'Shravan', 'Shakthi', 'Siva', 'Pritham', 'Jarvis', 'Srikanth', 'Devadarshan', 'Anjjai', 'Salha']

#I just got into a fight with Anjjai, so he isn't my friend anymore. I want to remove him using list.remove() method
friends.remove("Anjjai") 
print(friends) #['Manish', 'Deetchana', 'Tayeba', 'Nagarjun', 'Shravan', 'Shakthi', 'Siva', 'Pritham', 'Jarvis', 'Srikanth', 'Devadarshan', 'Salha']

#Having too many friends ain't good. I want to remove my last friend. I'll use list.pop() method for this
friends.pop() #Removes last element
print(friends) #['Manish', 'Deetchana', 'Tayeba', 'Nagarjun', 'Shravan', 'Shakthi', 'Siva', 'Pritham', 'Jarvis', 'Srikanth', 'Devadarshan']
print(friends.index("Pritham")) #7
print(friends.count("Siva")) #1
print(friends.sort()) #Sorts the list
friends.clear #None

#Now a list of lucky numbers
lucky_numbers = [4, 8, 15, 16, 23, 42] 
lucky_numbers.sort() 
print(lucky_numbers) #[4, 8, 15, 16, 23, 42]
lucky_numbers.reverse() #[42, 23, 16, 15, 8, 4]

numbers2 = lucky_numbers.copy() #Simply copies the list
print(numbers2) #[42, 23, 16, 15, 8, 4]