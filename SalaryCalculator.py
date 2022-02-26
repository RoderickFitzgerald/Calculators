#This calculator was to help teach my friend the importance of making sure superannuation was included in the wage.
#When you take out the general casual loading and super contribution, suddenly the pay doesn't look so great.
#In my own case it's significantly less than other offers around. But at a glance look better.


Is_Contracted = True
Superannuation_Included = False
Hours = 38
Duration = 52

Hourely_Rate = 40
SuperContribution = 10.5
CasualLoading = 20 #25% if going the other direction.

def Effective_Full_Time_Hourly_Rate():
    HourlyRate = ((Hourely_Rate / 100) * (100 - CasualLoading) / 100) * (100 - SuperContribution)
    return HourlyRate

def Effective_Full_Time_Weekly_Rate():
    WeeklyRate = (((Hourely_Rate / 100) * (100 - CasualLoading) / 100) * (100 - SuperContribution)) * Hours
    return WeeklyRate

def Effective_Full_Time_Monthly_Rate():
    MonthlyRate = ((((Hourely_Rate / 100) * (100 - CasualLoading) / 100) * (100 - SuperContribution)) * Hours) * (Duration / 12)
    return MonthlyRate

def Effective_Full_Time_Yearly_Rate(CalculateTax = False, Frequency = ""):
    YearlyRate = (((((Hourely_Rate / 100) * (100 - CasualLoading)) / 100) * (100 - SuperContribution)) * Hours) * Duration
    if (CalculateTax):
        return Tax_Calculator(YearlyRate, Frequency)
    return YearlyRate

def Tax_Calculator(Salary=70000, Frequency="Yearly"):
    result = 0
    if (Salary < 18200):
        return Salary
    elif (Salary < 45000):
        result = ((Salary - 18200) / 100) * (100 - 21) + 18200
        print("Bracket 1.")
    elif (Salary < 120000):
        result = ((Salary - 45001) / 100) * (100 - 34.5) + (45001 - 5092)
        print("Bracket 2.")
    elif (Salary < 180000):
        result = ((Salary - 120001) / 100) * (100 - 39) + (120001 - 29467)
        print("Bracket 3.")
    else:
        result = ((Salary - 180001) / 100) * (100 - 47) + (180001 - 51667)
        print("Bracket 4.")

    if (Frequency == "Hourly"):
        result = (result / 52) / 38
    elif (Frequency == "Weekly"):
        result = result / 52
    elif (Frequency == "Monthly"):
        result = (result / 52) * 12
    return result

print(str(Effective_Full_Time_Hourly_Rate()) + " After tax: " + str(Effective_Full_Time_Yearly_Rate(True, "Hourly")))
print(str(Effective_Full_Time_Weekly_Rate()) + " After tax: " + str(Effective_Full_Time_Yearly_Rate(True, "Weekly")))
print(str(Effective_Full_Time_Monthly_Rate()) + " After tax: " + str(Effective_Full_Time_Yearly_Rate(True, "Monthly")))
print(str(Effective_Full_Time_Yearly_Rate()) + " After tax: " + str(Effective_Full_Time_Yearly_Rate(True, "Yearly")))