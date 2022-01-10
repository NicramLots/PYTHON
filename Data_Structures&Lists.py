#This one shows how to create and how to reference a List in python
#Calling upon negative indexes works exactly as with all other methods in Python that is, the count is taken from the right to left

my_Values=[1,2,3,5.4,'dupa','cipa','cycki',000,12,'cycki']

print(my_Values[7])
print(my_Values[-1])
print(my_Values[-5][-1])
print(my_Values[1:])
print(my_Values[1:7])

#This one assigns a new value to an existing element in the List
print(my_Values[4])
my_Values[4]=666
print(my_Values[4])

#This one helps to identify at which location we can find a given characters

print(my_Values.index('cycki'))

#Converting List into boolean

my_List1=[]
my_List2=[1,2,3,4,'cycki',4.3]

print(bool(my_List1))
print(bool(my_List2))

print(my_List1,type(my_List1))

#This one clears a given list of any my_Values

#my_Values.clear()
#print(my_Values)

#This one copies a given list to a new content

my_List3=my_Values.copy()
print(my_List3)

#This one adds a new entry into the list at the very endswith

my_List3.append('cipcia')
print(my_List3)

#This one inserts a new value into the list but at a defined indexes

my_List3.insert(3,'cycuszki')
print(my_List3)

#This one extends a given list with new entries from another List

my_List4=[5,6]
my_List3.extend(my_List4)
print(my_List3)

#This one removes a given entry from the List
my_List3.remove('cycki')
print(my_List3)

#This one removes either (by default) the last entry in a list or an index defined entry in a List

print(my_List3)
my_List3.pop()
print(my_List3)
my_List3.pop(4)
print(my_List3)

#This one reverses the order of a given list

print(my_List3)
my_List3.reverse()
print(my_List3)

#This one sorts the data in ascending order

print(my_List3)
my_List3.clear()
print(my_List3)
my_List3=[9,2,4,1,7,5]
my_List3.sort()
print(my_List3)

#This one sorts the list in descending order

my_List3.sort(reverse=True)
print(my_List3)
