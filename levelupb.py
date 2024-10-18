

# dinosaurs = [ 
#     "Triceratops", 
#     "Velociraptor", 
#     "Ankylosaurus", 
#     "Archaeopteryx", 
#     "Tyrannosaurus Rex", 
#     "Stegosaurus", 
#     "Iguanodon"
#     ]

# saurus = []

# for i in dinosaurs:
#         if "saurus" in i:
#               saurus. append(i)

# print(saurus)

# saurus_dinosaurs = [i for i in dinosaurs if "saurus" in i]
# print(saurus_dinosaurs)

# coffee_order = (
#     "John - Latte",
#     "Manu - Hot Chocolate",
#     "Fereshta - Hot Water"
# )

# print(coffee_order)

# # tuples can not be append/ pop they are unchangeable
# # only .count and .index can be used on tuples

# print("type two numbers in two multiply them!")
# while True:
#     try:
#         num1 = int(input("First number:    >   "))
#         num2 = int(input("Second number:    >   "))
#         break
#     except ValueError:
#         print("Please only type in whole numbers!")
#     except TypeError:
#          print("Please only type in whole numbers!")
# print(num1 * num2)



# Activity 1



# truthy_or_falsy = [
#     0, 
#     "Hello!", 
#     " ", 
#     " !! ", 
#     12, 
#     True, 
#     None, 
#     "", 
#     "0", 
#     False, 
#     "False"
#     ]

# print(truthy_or_falsy)
# print("Using this list, write a program which checks each item," )
# print("and states if it is a Truthy or a Falsy value")

# for x in truthy_or_falsy:
#     bool(x)
#     #print(f"{x} is {bool(x)}")
#     # compare in terminal
#     if bool(x) == True:
#         print(f"{x} is truthy")
#     else:
#         print(f"{x} is falsy")
    

# Using this list, write a program which checks each item, 
# and states if it is a Truthy or a Falsy value.


# Activity 2
# Create two lists of names; a guest list and a barred list.
# Create a function which takes a guest’s name.
# If the name appears on the guest list, let the user know they can enter.
# If the name doesn’t appear on the guest list, let the user know they must wait.
# If the name appears on the barred list, the guest must get turned away.

# guest_list = [
#     "Manu",
#     "John",
#     "Tim",
#     "Mike",
#     "Liam"
#     ]

# barred_list = [
#     "Elliot",
#     "Hassan"
#     ]

# def check_guest():
#     name = input("Name Please: ").title()
#     if name in guest_list:
#         print(f"Right this way, {name.title()})")
#     elif name in barred_list:
#         print(f"Please leave, {name.title()})")
#     else:
#       print(f"You're not on the list, please wait {name.title()}.")
   
# check_guest()


# Activity 3
# Create a cash machine function (or functions!).
# The user must enter a correct pin and have enough funds to be allowed to withdraw an amount.
# Be creative.
# Once you have this functionality, expand!
# You could include more options, add a limit to the number of times the user can guess their pin, and more!

accounts = {     
    "account1": {"pin": "1234", "balance": 500},     
    "account2": {"pin": "5678", "balance": 1000} 
    }

print(accounts())


# Activity 4
# Take your apple buying program from day 2 of this course.
# Add error handling to it to ensure the input that the user gives can be converted to an integer.
# Handle the error appropriately to ensure a user can always try again until an integer is entered.