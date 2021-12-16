friends = ["Tayeba", "Kevin", "Kevin", "Salha", "Tayeba"]
print(friends)
print(friends[1])
friends[1]= "Mike"
print (friends[1])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.append("Kaden")
friends.insert(1, "Kelly")
print(friends)
friends.remove("Salha")
print(friends)
friends.pop() # remove last element of the list
print(friends)
print(friends.index("Bala"))
print(friends.count("Kevin"))
print(friends.sort())
friends.clear

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()

numbers2 = lucky_numbers.copy
print(numbers2)
