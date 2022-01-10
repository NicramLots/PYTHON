my_name="Nicram"
my_New_name="Nicrma Lots"
my_info="""
I Started my career
as a German Tax expert
and moved to Automation
"""

print(f'my name is {my_name}\nmy new name is {my_New_name}\nmy info is: {my_info}')

#To get a particular index character of a given string do the following:

print(my_name[0])

#It's possible to use negative indexes, that work right to left instead of left to right
#-1 index will always be the last character of a given string
print(my_name[-1])

#To print a range of characters based on indes, you need to provide it in this way:

print(my_name[0:4])

#To get the full length of the string you do it like this:\
print(my_name[0:])

#To get the length of a string...

print(len(my_name))

#To set a string to either Lower or Uppercase

my_String="THisISMyString"
print(my_String.lower())
print(my_String.upper())
print(my_String.title())
print(my_String.replace("MyStr","MyR"))

#THis is how you list all of the possible string operations on strings in Python

print(dir(my_String))

print(my_String.swapcase())
print(my_String.capitalize())

#This one converts everything into lower case however is stronger than the lower() method as it also converts certain special
#characters into their lower form like german letter B to ss

print(my_String.casefold())

#This method generates a boolean value based on whether the a codnition is fulfilled or not?

print(my_String.endswith("ping"))

print(my_String.__contains__("ping"))

#THe next one checks if a given string contains only spaces?

print(my_String.isspace())

#This next one checks if a given string contains only letters?

print(my_String.isalpha())

#This next one checks if a given string consists of both numbers and letters?

print(my_String.isalnum())

#THis one checks if a given string / variable is nummeric only in nature?

print(my_String.isnumeric())

#This one provides the full Help about all the string operations in Python

#help(str)

#This one joins particular characters of one variables with a define delimiter

my_String="Python"
y="-".join(my_String)
print(y)

#THis one centers a given string variable in a define numebr of characters

print(my_String.center(20))

#THis one justifies the text to the left
print(my_String.ljust(20))
#THis one justifies the text to the right
print(my_String.rjust(20))


#THis one fills in remaining places in a total number of characters with 0's.

print(my_String.zfill(30))

#This one removes spaces from back and front

my_String="  python   "
print(my_String.strip())

#This one removes a particular charatcter from a given strings but only if it appears at the beginning or the end of the string

my_String="python"
print(my_String.strip("p"))

#This one removes a particualr characgter / or string at either left or right side of the main strings

my_String="python is ma bitch python"

print(my_String.lstrip('python'))
print(my_String.rstrip('python'))

#THis one splits a given strings

my_String='Python is a very helpful language'
print(my_String.split()[1])
print(my_String.split('is')[0])

#THis one counts the number of occurances of a given character in a strings

print(my_String.count('i'))

#THis one gives the index of a given character / word in a string

print(my_String.index('is'))

#By adding a number after the comma we can decide from which index do we want to start to search for a given characer / word

print(my_String.index('e',14))

#THis one gives the option to find the index of a given character / word without error if the settings we provide do not match
#the content of the strings

print(my_String.find('is',30))

#This one does not relate to Python but is helpful

#type & path to a file = displays the contents of a given text file

#mode = displays the current setup of our command line
