# Basic Data types:
# Strings
# Integers
# Float
# Boolean

# -------------------------------
# 2.1 Data type exercise:

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# sum_str = int(two_digit_number[0]) + int(two_digit_number[1])
# print(sum_str)

# -------------------------------

# MATHEMATICAL OPERATIOS
#  + - * /
# PEMDASLR (i.e of priority in python calculations i.e BODMAS)
# Note: 
# + and - have equal priority but it depends which appear first from L to R
# * and / have equal priority but it depends which appear first from L to R

# -------------------------------

# 2.2 MBI calculator exercise:
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = int(weight)/( float(height) ** 2)
# print(int(BMI))

# -------------------------------

# 2.3 Life in weeks exercise:
# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# remaining_yrs = 90 - int(age)
# remaining_days = remaining_yrs * 365
# remaining_weeks= remaining_yrs * 52
# remaining_months = remaining_yrs * 12

# print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

# -------------------------------

# 2.4 A Tip Calculatpr exercise:

#If the bill was $150.00, split between 5 people, with 12% tip. 


#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

splitted_bill = total_bill / people
percentage_tip = total_bill * (tip/100)
splitted_tip = percentage_tip / people
individual_bill = round(splitted_bill + splitted_tip, 2)
final_bill = "{:.2f}".format(individual_bill)

print(f"Each person should pay: ${final_bill}")



