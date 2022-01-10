#Sample if / else statement in Python. For using = you have to write ==
x=2
y=3

if x<y:
    print("Cock")
else:
    print("Pussy")

#Artihmetic and Assignment Operators

#To define that something should be 'squared', you need to write **

x=3**9
print(x)

#To define a root of a number, you have to write // This root pull rounds the final value to its lowest values
#that means if the result is 3.5, the final root result will be 3
x=9//3
print(x)

#To calculate the 'reminder' of a division, you use module operator %

x=7%2
print(x)

x=8%2
print(x)

#Assignment operators assign values to particular variables. The main one is = but there are others like these occurances
a=3
b=4

a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)

#Comparatory Operators

'''
==
!=
>
<
>=
<=
'''
#This function provides the ascii representation of any string / character
ord('a')
print(ord('a'))

#This function provides a particular string / character from ascii to normal my_empty_tuple

print(chr(45))

#This section is dedicated to Identity Operators

'''
The examples of identithy operators is class/type/object

you can use:

is
is not

'''
x=1
y='Hi'
z=4
print(type(x) is type(y))
print(type(x) is type(z))
print(type(x) is not type(y))
print(type(x) is not type(z))

#This section is dedicated to Membership Operators

'''
These operators determine the membership of a value in a given object
example

x=[1,2,3,4,6]
6 in x

The typical membership operators are

in
not in
'''

x=[1,2,3,4,6]
print(6 in x)
y=7
print(y in x)

#More complex examples

valid_java=['1.6','1.7','1.8','1.9']
host_java='1.5'

if host_java in valid_java:
    print('host is included in valid java')
else:
    print('host is not included in valid java')

if host_java not in valid_java:
    print('host is included in valid java')
else:
    print('host is not included in valid java')

#This section is dedicated to Logical operators

'''
There are three types of logical operators in Python:

and
or
not
'''
#For AND, both operators must meet criteria for result to be TRUE
x=3>2 and 1 in [1,2,3]
print(x)

x=3>2 and 1 in [5,2,3]
print(x)

#For OR, at least one operator must meet criteria for result to be TRUE
x=3>2 or 1 in [5,2,3]
print(x)

#For NOT you are giving a contrary result from the one that would come either from an AND or OR logical operators

x=1<2
print(x)
x=not 1<2
print(x)

#ALL function can replace multiple ANDs

x=1<2 and 2<4 and 4<5 and 5<6
print(x)
x=all([1<2,2<4,4<5,5<6])
print(x)

#ANY fucntion can replace multiple others

x=1<2 or 2<4 or 4>5 or 5<6
print(x)
x=any([1<2,2<4,4>5,5<6])
print(x)
