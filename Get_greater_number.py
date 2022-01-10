#This is an example how to use the ELIF condition:

a=eval(input("Enter your first number: "))
b=eval(input("Enter your second number: "))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is less than {b}')
elif a==b:
    print(f'Both {a} and {b} are equal')
