#Basic script to see how long it'll take for you to pay off your student debt if you never got a pay increase / decrease.
from sys import argv

totalloanAmount = 60000 #Change this to your borrowed amount.
repaymentAmount = 5000  #Change this to your yearly repayments
indexAmount = 0.029
daysinyear = 365
years = 1
freedomIsReal = True
LongOutput = False

print(argv[0])
if len(argv) > 1:
    if argv[1].isdigit():
        totalloanAmount = int(argv[1])
if len(argv) > 2:
    if argv[2].isdigit():
        repaymentAmount = int(argv[2])
if len(argv) > 3:
    LongOutput = True


while totalloanAmount > 0 :
    i = 0
    origianlAmount = totalloanAmount
    while i != daysinyear :
        totalloanAmount = (totalloanAmount * (1 + indexAmount / daysinyear))
        i = i + 1
    if LongOutput : 
        print("Loan remaining: " + str(totalloanAmount))
        print("Years passed: " + str(years))
    if (origianlAmount < (totalloanAmount - repaymentAmount)):
        freedomIsReal = False
        break
    totalloanAmount = (totalloanAmount - repaymentAmount)
    if LongOutput: 
        print("Loan after payment: " + str(totalloanAmount))
    years = years + 1

if freedomIsReal == False :
    print("\n\nThe loan will never be paid off with current repayment.")
else:
    print("\n\nIt will take you " + str(years) + " at this rate to pay off your student loan.")