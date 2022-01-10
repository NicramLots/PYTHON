import os
t_w=os.get_terminal_size().columns

given_str=input("Enter your string: ")
print(given_str)
usr_option=input("Would you like to align your text? Enter 'LEFT', 'RIGHT' or 'CENTER'")
if usr_option=="CENTER":
    print(given_str.center(t_w).title())
if usr_option=="LEFT":
    print(given_str.ljust(t_w).title())
if usr_option=="RIGHT":
    print(given_str.rjust(t_w).title())
else:
    print('No alignment requested. Goodbye')
