import random
import my_module

# RANDOMISATION:

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.pi)

# random_float = random.random()
# print(random_float)

# selection = input('Heads or Tails? ')

# if selection == "Heads":
#     random_int = random.randint(0,1)
#     if random_int == 1:
#         print('You are right it is Heads. YOU WON')
#     else:
#         print('You are wrong it is Tails, YOU LOSE')

# elif selection == "Tails":
#     random_int = random.randint(0,1)
#     if random_int == 0:
#         print('You are right it is Tails. YOU WON')
#     else:
#      print('You are wrong it is Heads, YOU LOSE')    

# --------------------------------------------------------------------

# PYTHON LISTS

# names_string = input("Give me everybody's name. ")
# names = names_string.split(", ")
# random_int = random.randint(0, len(names))
# print(random_int)

# print(f"The one who is going to pay the bill is:{names[random_int - 1]}")

# --------------------------------------------------------------------

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# horizontal  = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = " X"
# print(f"{row1}\n{row2}\n{row3}")


# --------------------------------------------------------------------



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rock_paper_scissors = [rock, paper, scissors]

user_input= input("What do you choose? ").lower()
computer_int = random.randint(0, len(rock_paper_scissors)- 1)

# users choice
if user_input == "rock":
    user_choice = rock_paper_scissors[0]
    print(user_choice)

elif user_input == "paper":
    user_choice = rock_paper_scissors[1]
    print(user_choice)

elif user_input == "scissors":
    user_choice = rock_paper_scissors[2]
    print(user_choice)

# computer's choice
if computer_int == 0:
    computer_choice = rock_paper_scissors[0]
    print(computer_choice)

elif computer_int == 1:
    computer_choice = rock_paper_scissors[1]
    print(computer_choice)

elif computer_int == 2:
    computer_choice = rock_paper_scissors[2]
    print(computer_choice)



    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.
    # rock =0, paper =1, scissors =2

if(user_choice == rock_paper_scissors[0] and computer_choice == rock_paper_scissors[2]):
    print("---YOU WIN---")

elif (user_choice == rock_paper_scissors[2] and computer_choice == rock_paper_scissors[0]):
    print("---YOU LOSE---")

elif (user_choice == rock_paper_scissors[2] and computer_choice == rock_paper_scissors[1]):
    print("---YOU WIN---")

elif (user_choice == rock_paper_scissors[1] and computer_choice == rock_paper_scissors[2]):
    print("---YOU LOSE---")

elif (user_choice == rock_paper_scissors[1] and computer_choice == rock_paper_scissors[0]):
    print("---YOU WIN---")

elif (user_choice == rock_paper_scissors[0] and computer_choice == rock_paper_scissors[1]):
    print("---YOU LOSE---")
else:
    print("---ITS A TIE---")












