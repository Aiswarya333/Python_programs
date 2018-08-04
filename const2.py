'''MONTH NAME TO NUMBER OF DAYS - The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the
user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.'''

month=input('ENTER THE NAME OF THE MONTH    :')

if month in ("January","March","May","July","August","October","December"):
    print("NUMBER OF DAYS IN THE MONTH  : 31days")
elif month=="February":
    print("NUMBER OF DAYS IN THE MONTH  : 28/29days")
elif month in ("April","June","September","November"):
    print("NUMBER OF DAYS IN THE MONTH  : 30days")
