#To define a set in Python, you have to use curly brackets but not as in dictionaries with key / value settings
#but simply values divided with commas

#This is a dictionary
my_set={'dupa':'123'}
print(my_set['dupa'])

#This is a set
my_set.clear()
print(my_set)
my_set={1,7,0,3,3,3,4,2,9}
print(my_set)

#In sets, data is sorted automatically in ascending order also, if there are any duplicates, those duplicates will
#also be removed

#To define an empty set (and not dictionary) you have to write it this always

my_new_set=set({})
print(type(my_new_set))

#To convert a list into a set, do the following

my_li=[1,3,4,9,3,3,2,34,0,'cipka',123,'cycki']
print(my_li,type(my_li))
my_li2=set(my_li)
print(my_li2,type(my_li2))
my_li3=list(my_li2)
print(my_li3,type(my_li3))

#This is how you join settings

a={1,6,3,5,4}
b={5,9,10,11,12,23}
print(a.union(b))
print(a.intersection(b))
