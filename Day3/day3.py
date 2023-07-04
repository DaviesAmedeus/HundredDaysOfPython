# CONDITIONALS

# -----------------------------------------------------------
#3.1 Odd or Even Exercise
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))


# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI = round(weight / (height ** 2), 1)

# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are UNDERWEIGHT")
# else:
#     if BMI < 25:
#         print(f"Your BMI is {BMI}, you are NORMAL WEIGHT")
#     elif BMI < 30:
#         print(f"Your BMI is {BMI}, you are OVERWEIGHT")
#     elif BMI < 35:
#         print(f"Your BMI is {BMI}, you are OBESE")
#     else:
#         print(f"Your BMI is {BMI}, you are CLINICAL OBESE")
              
# -----------------------------------------------------------
 

#3.2 Leap year exercise:
# year = float(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 != 0:
#         if year % 400 != 0:
#             print("Leap Year")
#         else:
#           print("NOT Leap Year") 
#     else:
#      print("NOT Leap Year")

    
# else:
#     print("NOT Leap Year")

# -----------------------------------------------------------

#3.4 Pizza order exercise:
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if size == "S":
#     bill = 15

#     if add_pepperoni == "Y":
#         bill+=2


# elif size == "M":
#     bill = 20

#     if add_pepperoni == "Y":
#         bill+=3

# elif size == "L":
#     bill = 25

#     if add_pepperoni == "Y":
#         bill+=3

# if extra_cheese == "Y":
#     bill+=1

# print(f"Your final bill is ${bill}")

# -----------------------------------------------------------


# Logical Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")


# -----------------------------------------------------------

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# lowercase_name1 = name1.lower()
# lowercase_name2 = name2.lower()

# counts for TRUE
# t = lowercase_name1.count("t") + lowercase_name2.count("t")
# r = lowercase_name1.count("r") + lowercase_name2.count("r")
# u = lowercase_name1.count("u") + lowercase_name2.count("u")
# e = lowercase_name1.count("e") + lowercase_name2.count("e")

# true = str(t + r + u + e)

# counts for LOVE
# l = lowercase_name1.count("l") + lowercase_name2.count("l")
# o = lowercase_name1.count("o") + lowercase_name2.count("o")
# v = lowercase_name1.count("v") + lowercase_name2.count("v")
# e = lowercase_name1.count("e") + lowercase_name2.count("e")

# love = str(l + o + v + e)

# love_score = true + love

# love_score_as_int = int(love_score)

# if (love_score_as_int) < 10 or (love_score_as_int > 90):
#     print(f"Your score is {love_score_as_int}, you go together like coke and mentos.")
# elif (love_score_as_int >= 40) and (love_score_as_int <= 50):
#     print(f"Your score is {love_score_as_int}, you are alright together.")
# else:
#     print(f"Your score is {love_score_as_int}.")


# -----------------------------------------------------------

# print("Welcome to Treasure Alien Island.")
# print("Your mission is to find the treasure.") 

#Write your code below this line 👇

# direction = input("LEFT or RIGHT? ").lower()
# if direction == "left":
#     choice = input("SWIM or WAIT").lower()
#     if choice ==  "swim":
#         print("---GAME OVER----")
#     elif choice == "wait":
#         door = input("Which door? BLUE, RED or YELLOW ").lower()
#         if door == "yellow":
#             print("---YOU WIN----")

#         if door == "blue":
#             print("---GAME OVER----")
        
#         if door == "red":
#             print("---GAME OVER----")

# elif direction == "right":
#     print("---GAME OVER----")