#This is a script which you put in the amount of money that you want to earn in the future for passive income.
#Apparently argv0 on Windows is the script itself, neato.

import sys

PayoutTarget = 400000
InvestmentTarget = 2000000
InvestmentInput = 2100 #Monthly
TotalInvested = 0
GrowthRate = 0.09
Payout = 0
Years = 0
Months = 0

print(sys.argv[0])

if sys.argv[1].isdigit():
    PayoutTarget = int(sys.argv[1])
if sys.argv[2].isdigit():
    InvestmentInput = int(sys.argv[2])


while Payout < PayoutTarget :
    while Months < 12 : 
        TotalInvested = TotalInvested + InvestmentInput
        Months = Months + 1
        #print(Months, TotalInvested)
    Months = 0
    TotalInvested = TotalInvested * (1 + GrowthRate)
    Payout = TotalInvested * (GrowthRate / 2)
    Years = Years + 1
    #print(str(Payout) + " " + str(Years))

print(str(Payout) + " " + str(Years))
