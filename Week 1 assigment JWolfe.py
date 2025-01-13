# 1.
#pet name and type
pet_type = "dog"
pet_name = "Max"

#print pet type and name
print(f"I have a {pet_type} and his name is {pet_name}.")


# 2.
#input statements from user
first_name = input("Enter your first name? ")
current_age = int(input("Enter your current age? "))
yearly_savings = float(input("Enter your yearly savings? "))

#Math
age_10_years = current_age + 10

#Printing user information
print(f"Hello {first_name}, you are currently {current_age} years old.")
print(f"in 10 years, you will be {age_10_years} years old.")


# 3.
#import data
import calendar
from datetime import datetime

#get month and year
now = datetime.now()
current_year = now.year
current_month = now.month

#days in month
days_month = calendar.monthrange(current_year, current_month)[1]

#convert to seconds
seconds_day = 24 * 60 * 60
seconds_month = days_month * seconds_day

#print results
print(f"The number of seconds in the current month is {seconds_month} ")


#4
#number of eggs
num_egg = int(input("Enter the number of eggs: "))

#calculate dozens & remainders
dozen = num_egg // 12
extra_eggs = num_egg % 12

#eggs in basket
print(f"This makes {dozen} dozen eggs with {extra_eggs} eggs left over.")
