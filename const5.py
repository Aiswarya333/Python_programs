'''CELL PHONE BILL - A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month. Each additional minute of air time costs
$0.25, while additional text messages cost $0.15 each. All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill
(including the 911 charge) is subject to 5 percent sales tax.
Write a program that reads the number of minutes and text messages used in a month from the user. Display
the base charge, additional minutes charge (if any), additional text message charge (if any), the 911 fee, tax and total bill amount. Only display the additional
minute and text message charges if the user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal places.'''

min=int(input('ENTER THE NUMBER OF MINUTES  :'))
msg=int(input('ENTER THE NUMBER OF MESSAGES :'))
BASE_COST=15.00
MSG_COST=0.15
CALL_COST=0.25
accost=0.0
amcost=0.0

if min>50:
    accost=(min-50)*CALL_COST
if msg>50:    
    amcost=(msg-50)*MSG_COST
center=amcost+accost+BASE_COST+0.44 
tax=(BASE_COST+amcost+accost+center)*5/100
total=tax+BASE_COST+amcost+accost+center

print('''
       BASE CHARGE                 :  %.2f
       ADDITIONAL MINUTES CHARGE   :  %.2f
       ADDITIONAL TEXT CHARGE      :  %.2f
       911 FEE                     :  %.2f
       TAX                         :  %.2f
       ------------------------------------------
       TOTAL BILL AMOUNT           :  %.2f
       ''' %(BASE_COST,accost,amcost,center,tax,total))



