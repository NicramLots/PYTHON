#simple arythmetic calculator
import random
a = random.randint(0,999)
b = random.randint(0,999)

result=a+b

print(f"The addition of {a} and {b} equals to {result}")

result=a*b

print(f"The multiplication of {a} by {b} equals to {result}")

a = int(input("Enter the value for A"))
b = int(input("Enter the value for B"))

result=a+b

print(f"The addition of {a} and {b} equals to {result}")

result=a*b

print(f"The multiplication of {a} by {b} equals to {result}")

#Using the evaluation function to determine the type of a variable comming from input command

a = eval(input("Enter the value for A"))
b = eval(input("Enter the value for B"))

result=a+b

print(f"The addition of {a} and {b} equals to {result}")

result=a*b

print(f"The multiplication of {a} by {b} equals to {result}")
