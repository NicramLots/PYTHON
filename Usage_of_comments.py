#This is a simple calculator
#created by Nicram
#Dated: 2021.12.06

'''
This section is to be commented out with the help of three quotes.
This is fairly easy and handy if you need to comment out mulitple lines at one time
'''


from datetime import date

today = date.today()
print("Today's date: ", today)

myFirstvar = 7
mySecondVar = 10
result = myFirstvar + mySecondVar
print(f"The sum of {myFirstvar} and {mySecondVar} is {result}")

if result>20:
    print("The result is bigger than 20.\nThis result also includes a line break.")
else:
    print("The result is smaller than 20.\nThis result also includes a line break.")
print("python's Scripts are cool")
print("This is a \"python class\"")
print("C:\\OTHER\\DEV\\PYTHON")
