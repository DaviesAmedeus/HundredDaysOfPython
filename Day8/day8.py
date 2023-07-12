import math
# # function that allows inout
# def great_with_name_and_location(name,location):
#     print(f"Hello {name}")
#     print("How do you do?")
#     print(f"Isn't the weather nice today in {location}")
 
# great_with_name_and_location(location="Davies", name="Buguruni")

#Write your code below this line 👇


# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     cans = math.ceil(number_of_cans)
#     print(f"You'll need {cans} cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# --------------------------------------------------------

#Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is a prime number")
#     else:
#         print("Its not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# e

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
       end_text += char
        
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'Y' if you want to go again. Otherwise 'NO: \n").lower()
    if result == "no":
       should_continue = False
       print("GOODBYE!")
