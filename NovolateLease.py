#Hopefully this is useful.
#This was mostly used for a Skoda Superb Sportsline Wagon 4x4 206TSi.
#I put in the price at like, $12k off the offer I got today.
#The real thing to look into is FBT.
#What you need to do is figure out how to reduce your FBT to 0 for the employer.
#So if you get taxed like 34.5% like most Australian's you can effectively calculate that tax as apart of your pay raise.
#If you go for a Novated Lease. Which I am debating because that car is fun and very spacious and noice.

#CurrentCar
ccPetrol = 75
ccRego = 950
ccService = 400
ccInsurance = 1200

ccTotalCost = 0

print("\n\nThis is the current running costs of my vehicle, hurrah!, Hurrah!\n\n")

def YearlyCostIntoWeekly():
    YearlyPetrol = ccPetrol * 52
    ccTotalCost = YearlyPetrol + ccService + ccRego + ccInsurance
    print("Total weekly cost of my current car: " + str(round(ccTotalCost / 52)))
    print("Total monthly cost of my current car: " + str(round(ccTotalCost / 12)))
    print("Total yearly cost of my current car: " + str(round(ccTotalCost)))

YearlyCostIntoWeekly()

tileWal = '~' * 80 + '\n'

print('\n' +'\n' + tileWal + tileWal + tileWal + '\n')

def NovatedInterest():
    VehiclePrice = 60000
    InterestRate = 0.045
    TermOfLease = 5
    ResiduialValue = 0.2813 #Percentage.
    EffectivePrice = VehiclePrice - (VehiclePrice * ResiduialValue)
    BaseValue = EffectivePrice / TermOfLease

    i = 0
    TotalOwed = 0
    while TermOfLease > i:
        YearlyOwed = BaseValue + (EffectivePrice * InterestRate)
        TotalOwed += YearlyOwed
        EffectivePrice -= BaseValue
        print("Year: " + str(i+1) + " has a repayment of: $" + str(round(YearlyOwed, )))
        i += 1
    print("\nTotal repayments are: $" + str(round(TotalOwed, 2)))
    print("The remaining value of the vehicle to own is: $", str(round(VehiclePrice * ResiduialValue, 2)))
    print("The total cost of ownership for this vehicle is: $" + str((VehiclePrice * ResiduialValue) + TotalOwed))





NovatedInterest()