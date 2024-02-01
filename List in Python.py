#friends = ["Smriti", "lippi ", "Sonu","Sanchi", "Ankur"]
#print (friends[-1])
#print (friends[-3])
#print (friends[1:])
#print (friends[1:3])
#print (friends[1:])

#if we want to  modify 
#friends[1]="michael"
#print(friends[1])

#List Function in python
lucky_numbers = [4, 8, 25, 16, 23, 42 ]
friends = ["Smiriti", "lippi ", "Sonu","Sonu","Sanchi", "Ankur"]
friends.extend(lucky_numbers)
friends.append("Satendra") #add item in the end of the list 
friends.insert(4,"Rupali")
friends.remove("Sanchi")
#friends.clear()
#friends.pop()
#print(friends.index("Sonu"))
#print (friends.count("Sonu"))
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
 
