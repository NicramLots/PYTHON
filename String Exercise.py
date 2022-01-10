import os
os.get_terminal_size()
my_size=os.get_terminal_size().columns

given_str=input("Enter your value here: ")

print(given_str.center(my_size).title())
print(given_str.ljust(my_size).title())
print(given_str.rjust(my_size).title())
