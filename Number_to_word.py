#THe below example is an example where every single condition is checked:
'''
numb=eval(input('Provide your number from a 1 to 10 range: '))
if numb==1:
    print("one")
elif numb==2:
    print("two")
elif numb==3:
    print("three")
elif numb==4:
    print("four")
elif numb==5:
    print("five")
elif numb==6:
    print("six")
elif numb==7:
    print("seven")
elif numb==8:
    print("eight")
elif numb==9:
    print("nine")
elif numb==10:
    print("ten")
elif numb not in [1,2,3,4,5,6,7,8,9,10]:
    print("The number you provided is out of range from the available range.")
'''

#The below example is one where we have a quicker way to identify if the provided number is in a defined range:

numb=eval(input('Provide your number from a 1 to 10 range: '))
numb_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if numb in [1,2,3,4,5,6,7,8,9,10]:
    print(numb_word.get(numb))
else:
    print('The value you provided is out of the accepted range. Next time provide a different number')
