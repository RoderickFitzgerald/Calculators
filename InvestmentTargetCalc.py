#This is a script which you put in the amount of money that you want to earn in the future for passive income.
#Apparently argv0 on Windows is the script itself, neato. 
#I am debating making the same calculator but with an effective monetary value.
#This is like when you look at how much $200 was in 1960 and you're like wow that really was a lot in todays money.
#Similar to that as we go further in the future the more money we have the less effective it actually is.
#Still having millions in the future is a lot of money though.

from sys import argv

PayoutTarget = 400000 #My target of $400,000 
InvestmentTarget = 2000000 #Unused but I might use later.
InvestmentInput = 2100 #Monthly, more aggressive than I think I can do.
TotalInvested = 0
GrowthRate = 0.09 #This is on company bonds, some places have reporting around 9% rate which is massive.
Payout = 0
Years = 0
Months = 0

print(argv[0])
if len(argv) > 1:
    if argv[1].isdigit():
        PayoutTarget = int(argv[1])
if len(argv) > 2:
    if argv[2].isdigit():
        InvestmentInput = int(argv[2])


while Payout < PayoutTarget :
    while Months < 12 : 
        TotalInvested = TotalInvested + InvestmentInput
        Months = Months + 1
    Months = 0
    TotalInvested = TotalInvested * (1 + GrowthRate)
    Payout = TotalInvested * (GrowthRate / 2)
    Years = Years + 1

print()
print("You have $" + '{:,}'.format(round(TotalInvested, 2)) + " invested which generates you passively, $" + '{:,}'.format(round(Payout, 2)) + " each year.")
print("It took you a total of: " + str(Years) + " years to achieve.")
