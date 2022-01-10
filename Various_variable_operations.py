#The below fucntion gives the allocation of a variable in RAM memory
x=4
print(id(x))

id_x=id(x)
print(id_x)
#This is how you can decalre and later delete a variable

x=4
print(x)
del x

#This part represents how multiple variables can be defined in one lines
x=3;y=5.6;z=3+4j
print(x);print(y);print(z)

print(x,y,z)
#This part gives the type of each variables
print(x,type(x))
print(y,type(y))
print(z,type(z))

#This part represents a string

my_name="Nicram Lots"
print(my_name)
my_name='Nicram Lots'
print(my_name)

#THis part represents a Boolean variable - Boolean variables always need to written with Uppercase (first letter)
#otherwise you get an error as the lowercase entry is identified as a variable that is not present

x=True
y=False
print(x)
print(y)

#This part shows how to convert variables from one type to another

x=56
print(x,type(x))
y=str(x)
print(y,type(y))
z=bool(x)
print(z,type(z))

#THis part represents how complex values are converted into integer - it is important that with this conversion, the decimals are dropped, not rounded

x=5.6
print(int(x))

#THere is a data type called None

None
print(None)

#This fucntion below allows to print varibales in different always
x=1
y=3.5
z="dupa"

print("{} {} {}".format(z,y,x))
print("{} \n{} \n{}".format(z,y,x))

# Writing with {}

print(f"x value is: {x} \ny value is {y} and \nz value is {z}" )

#Another way of writing variable values in a string

my_Output = f"x value is: {x} \ny value is {y} and \nz value is {z}"
print(my_Output)
