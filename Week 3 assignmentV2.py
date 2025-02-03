# 1. get user to input name and greet them

x = input ("Please enter your name: ")
print("Hello "+x,"!")


# 2. get user to input age (explain error)
# error TypeError: can only concatenate str (not "int") to str cannot convert w/o int function
x1 =  input("whats'up your age? ")
x1 = int(x1)
print (x1 + 5)

# 3. Use concatenation and str() to print a message telling the user how old they will be in y years.
# get users age and how many years to add
age_input = input(x + " please enter your age: ")
how_old = input(x + " please enter how many years to add to you age: ")
# convert to intergers and calculate
age = int(age_input)
old = int(how_old)
print (x + " your age in " + str(old) +" years you will be: " + str(age + old))


# 4. Ask the user to enter values that might be floating point.
# get user input for hours worked and hourly wage
hours_worked = float(input(x + " How many hours did you work? "))
hourly_wage = float(input(x + " Enter your hourly wage without the $: "))
# calculate total
week_total = hours_worked * hourly_wage
# output results
print(x + f" your total payment for this weeks paycheck is: ${week_total:.2f}")


#5.  Print out the result of the calculation in a single print statement, using concatenation.
# get user input for hours worked and hourly wage
hours_worked = float(input(x + " enter number of hours worked? "))
hourly_wage = float(input(x + " Enter your hourly wage without the $: "))
# calculate total hours assuming 40/hrs a week 50 weeks/year
week_total = hours_worked * hourly_wage
anual_gross = hourly_wage * 40 * 50

# Tax..(nightmare) bracket
if anual_gross <= 11600:
    tax_rate = .1
elif anual_gross <= 47150:
    tax_rate = .12
elif anual_gross <= 100525:
    tax_rate = .22
elif anual_gross <= 191950:
    tax_rate = .24
elif anual_gross <= 243725:
    tax_rate = .32
elif anual_gross <= 609350:
    tax_rate = .35
else:
    tax_rate = .37
# math after taxes
anual_after_tax = anual_gross * (1 - tax_rate)
# print the results
print(f""" Your gross pay this week is $ {round(week_total, 2)}.
Your estimated annual gross pay will be $ {round(anual_gross, 2)}.
After taxes, your estimated annual income will be $ {round(anual_after_tax, 2)}.""")
