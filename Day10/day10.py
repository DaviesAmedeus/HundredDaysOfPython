# function with outputs

# def format_name(f_name, l_name):
#     result_f_name = f_name.title() 
#     result_l_name = l_name.title()

#     return (f"{result_f_name}  {result_l_name}")

# formate_string = format_name("davies", "edgar")
# print(formate_string)

# ----------------------------------------------------------------

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True 
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) and  month == 2:
#     return 29 
#   return month_days[month -1]

  
#🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# ----------------------------------------------------------------

# CALCULATOR

def add(n1, n2):
    return n1 + n2

def substruct(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substruct,
    "*": product,
    "/": divide

}

def calculator():
    num1 = float(input("What's the first number?: "))


    for symbol in operations:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_funtion = operations[operation_symbol]
        answer = calculation_funtion(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        direction = input("Do you want to continue? Y/N: ").lower()
        if direction == "y":
            continue_calculation = True
            num1 = answer
        else:
            continue_calculation = False
            calculator()


calculator()      