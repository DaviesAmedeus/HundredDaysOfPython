# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
    
# }

# Retrieving items from dictonary
# print(programming_dictionary["Bug"])

#Adding new items in a dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again" 
# print(programming_dictionary)

# wipe an existing dictionary (cleaning)
# programming_dictionary = {}
# print(programming_dictionary)

#Editing items in a dictionary
# programming_dictionary["Bug"] = "----------------------" 
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#     print(f"{key} -> {programming_dictionary[key]}")
    

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# student_grades = {}


# for key in student_scores:
#     if student_scores[key] >= 91 and student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"

#     elif student_scores[key] >= 81 and student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectationd"

#     elif student_scores[key] >= 71 and student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"



# # 🚨 Don't change the code below 👇
# print(student_grades)

# -----------------------------------------------------------------------

# NESTING LISTS INSIDE DICTIONARIES
# travel_log = {
#     "Francee": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgsrt"], 
# }

# travel_log = {
    
#         "France":{
#             "cities":["Paris", "Lille", "Dijon"],
#             "total_visitie": 12
#             },
#         "Germany": {
#             "cities":["Berlin", "Hamburg", "Stuttgsrt"],
#             "total_visitie": 6
#             }, 
  
# }

#-------------------------------------------------------------------------------

# NESTING DICTIONARIES INSIDE lists
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# def add_new_country(country, visits, cities = []):
#         new_country = {}
#         new_country["country"] = country,
#         new_country["visits"] = visits
#         new_country["cities"] = cities
#         travel_log.append(new_country)




#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# from art import logo
# import os
# clear = lambda: os.system('clear')

# print(logo)
# print("Welcome to secret auction Program by Davies Amedeus")

# def find_highest_bidder(auction_dictionary):
#     highest_bid =0
#     winner = ""

#     for bidder in auction_dictionary:
#         bid__amount = auction_dictionary[bidder]
#         if bid__amount > highest_bid:
#             highest_bid = bid__amount
#             winner = bidder
#         print(f"The winner is {winner} with a bid of ${highest_bid}")


# auction_dictionary = {}
# bid_direction = True

# while bid_direction ==True:
#     name = input("Enter Your Name: ")
#     bid_price = int(input("What's your bid price in Tsh: "))

#     auction_dictionary[name] = bid_price
#     print(auction_dictionary)

#     continue_qn = input("Is there other who wants to bid: ").lower()
#     if continue_qn == "no":
#         bid_direction = False
#         find_highest_bidder(auction_dictionary)

#     elif continue_qn == "yes":
#         clear()
#         bid_direction = True
    
#     else:
#         bid_direction = False


auction_record = {
    "Davies": 100,
    "Edgar": 700,
    "Mariana": 200
}


highest_bid = 0
highest_bidder = ""

for name in auction_record:

    if auction_record[name] > highest_bid:
        highest_bid = auction_record[name]
        highest_bidder = name

print(f"The highest bid is {highest_bid} by {highest_bidder}")