# ux = dollar amounts for individual trips

# uxm = miles driven for each trip, with 20 flat tacked on
# for time driving between trips, to surge zones, and to/from home

# uxh = total hours worked

# To do overarching numers, create one or more variables to input your historical numbers
# utilizing your payment statements. This is meant to be utilized in an ongoing manner, and
# requires keeping your books up to date. However this can be leveraged to calculate performance
# as an average across all ridesharing services that you decide to partner with, and compare who
# deserves your effort the most. 

# Future versions will could include GUI or API to input trip rates, mileage, and hours.

# DATES WORKED:
# 6/23
u1 = 10.8 + 5 + 7 + 8.89 + 7.72 + 16.43 + 5
u1m = 5.18 + 1.19 + .39 + 3.07 + 3.29 + 10.57 + 20
u1h = 3.0
# 6/25
u2 = 11.7 + 8.13 + 7.87 + 5 + 5
u2m = 6.34 + 3.42 + 2.73 + .61 + .66 + 20
u2h = 2.0

# I realize that it would be better to create classes or arrays of data to iterate over
# but this is what happens when you've only completed 9 pages of LPTHW exercises

# CALCULATOR VARIABLES:
# pretax earnings is all the income reported from the app for all your trips
pretax_earnings = u1 + u2

# uber deduction is a flat 20% taken off the top 
uber_deduction = pretax_earnings * .2

# tax shows the maximum dollar amount that should be saved for filing season
# 35% is the average payroll deduction, but may vary, and can be reduced
tax = (pretax_earnings - uber_deduction) * .35

# posttax earnings shows earnings after tax, but before gas
posttax_earnings = pretax_earnings * .65

# another option is to do odometer readings before you start and stop working. 
# this calculates total miles, plus the extra 20 miles each work day as a baseline (extra)
total_miles = u1m + u2m

# gas used calculates gallons of gas used based on your cars mileage
# simply replace the '21' with your cars mileage
gas_used = total_miles / 21

# mileage cost calculates the cost of the gas you've used
# simply replace '3.15' with your car's mileage
mileage_cost = gas_used * 3.15

# takehome calculates the difference between posttax earnings and mileage costs
# this amount is your total 'profit'. Future versions may include a cost per mile
# to calculate wear and tear costs on your vehicle. 
takehome = posttax_earnings - mileage_cost

# hours worked calculates your total hours worked
hours_worked = u1h + u2h

hourly_rate = takehome / hours_worked

print "You earned a total of $%d." % pretax_earnings
print "You need to save a maximum of $%d for taxes." % tax
print " "
print "You've driven roughly %d miles, using %d gallons of gas." % (total_miles, gas_used)
print "You've paid $%d for gas on Uber trips, not including wear and tear." % mileage_cost
print " "
print "Uber's %s cut of your trips is $%d." % ('20%', uber_deduction)
print "Your takehome pay for %d hours, after gas and tax is $%d." % (hours_worked, takehome)
print "You earned an average of %d per hour, after gas and taxes." % hourly_rate