#Basic script to see how long it'll take for you to pay off your student debt if you never got a pay increase / decrease.

repaymentAmount = 2275  #Change this to your yearly repayments
totalloanAmount = 59000 #Change this to your borrowed amount.
indexAmount = 0.029
daysinyear = 365
years = 1

while totalloanAmount > 0 :
    i = 0
    while i != daysinyear :
        totalloanAmount = (totalloanAmount * (1 + indexAmount / daysinyear))
        i = i + 1
    print("Loan remaining: " + str(totalloanAmount))
    print("Years passed: " + str(years))
    totalloanAmount = (totalloanAmount - repaymentAmount)
    print("Loan after payment: " + str(totalloanAmount))
    years = years + 1

print("It will take you " + str(years) + " at this rate to pay off your student loan.")