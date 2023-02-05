#This code is a age calculator, in which the max age expected is 90 years.
#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months  

age = int(input("What is your age in years: "))

left_days = ((90*365) - (age*365))
left_weeks = ((90*52) - (age*52))
left_months = ((90*12) - (age*12))

print(f"You have left {left_days} days, {left_weeks} weeks, and {left_months} months")