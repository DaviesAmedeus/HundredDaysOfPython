# AVERAGE HEIGHT EXERCISE

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# sum = 0
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   n+=1
#   sum += student_heights[n-1]

# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# average = round(sum/n)
# print(average)

# ---------------------------------------------------------------

# HIGH SCORE EXERCISE

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# top_score = 0
# for score in student_scores:
#   if score > top_score:
#     top_score = score

# print(f"The highest score in the class is: {top_score}")

# ---------------------------------------------------------------


# total = 0

# for number in range(2,101, 2):
#   total+= number

# print(total)

# ---------------------------------------------------------------

# FIZ BUZZ EXERCISE

# for number in range(1,101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")

#   elif number % 3 == 0:
#     print("Fizz")
  
#   elif number % 5 == 0:
#     print("Buzz")
  
  
#   else:
#     print(number)

# ---------------------------------------------------------------

#PASSWORD GENERATOR PROJECTOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# random_letters = ""
# random_numbers = ""
# test_letters = random.randint(0, nr_letters)
# selected_letters="" 
# selected_symbols = ""
# selected_numbers = ""


# for letter in range(0, nr_letters):
#     random_letters = random.randint(0, 51)
#     selected_letters += letters[random_letters]
# print(selected_letters)
# print('\n')
  
# for symbol in range(0, nr_symbols):
#     random_symbols = random.randint(0, 8)
#     selected_symbols += symbols[random_symbols]
# print(selected_symbols)    
# print('\n')

# for number in range(0, nr_numbers):
#     random_numbers = random.randint(0, 9)
#     selected_numbers += numbers[random_numbers]
# print(selected_numbers)
# print('\n')

# password = selected_numbers + selected_letters + selected_symbols
# print(password)


# ALTERNATIVE
# Eazy Level
password =[]

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)


# Eazy Level
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

password_string= ""
for char in password:
    password_string += char

print(f"Your password is:: {password_string}")