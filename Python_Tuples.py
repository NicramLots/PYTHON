#This one defines an empty Tuple setup
my_empty_tuple=()
print(my_empty_tuple)
#This one defines a Tuple with some elements
my_full_tuple=(1,3,4,9,3)
print(my_full_tuple)

#Tuples can consist of single elements as well as of elements that are lists

my_tuple=(2,4,1,[4,3,9],0,2)
print(my_tuple)

#To call upon a gien tuple element using index, you apply the same brackets as for lists
print(my_tuple[3])
#To get to the inner index of the list that is a part of the tuple, use this\
print(my_tuple[3][1])

my_new_element=(19,)
my_tuple=my_tuple+my_new_element
print(my_tuple)

#Tuples are immutable that means you cannot add or remove elements from them, when updating you need to re-assign the my_Values

print(my_tuple[0:])

#To defien decimals in python, you use . and not , commas are used to point at a variable being a Tuples
