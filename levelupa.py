# music = "classical"
# shopping_list = ["a"]
# num = 0
# name = ""
# my_name = "Dave"

# print(bool(music))
# print(bool(shopping_list))
# print(bool(num))
# print(bool(name))
# print(bool(my_name))


# add = input("add to list: ")

# while add != shopping_list:
#     add = input("add to list: ")
#     print(shopping_list)
#     shopping_list.append(add)

# print(shopping_list)

# def add_up(num1,num2):
#     return num1+num2

# add_up(4,7)
# print(add_up(4,7))

# Activity 1
# Write a list of your favourite books. 
# Create a program which allows a user to type in their favourite 
# book. 
# If their favourite book matches one of your favourite books print 
# “<bookname> is one of my favourite books too.”
# Else, print “I haven’t read that book.”
# Ensure the user gives you information - a blank string should not 
# be accepted!

# changed to cars 

fav_car = [
    "bmw",
    "dodge",
    "audi"
]
# list of my fav cars

r = "I like too!"
# responce to same user input
w = "I dont like!"
#responce to other inputs

user_car = input("Enter car brand: ").lower()
#user enter car brand

while user_car == "" or user_car == " ":        
    print("You didn't enter anything! Please type car brand.")        
    user_car = input("Enter car: ")
# loops until user enters something, a blank string is not accepted!

if user_car in fav_car:        
    print(f"{r} {user_car.title()}'s are nice")
else:    
    print(f"{w} {user_car.title()}'s are not nice")




# list_of_favourite_books = []

# def add_a_book(book):
# list_of_favourite_books.append(book)

# def check_list_for_book(book):
# return book in list_of_favourite_books

# def ask_for_a_fav_book():
# return input("\nhhat is your favourite book? ").capitalize()

# fav_book = ask_for_a_fav_book()

# while fav book != "Done":
# if fav_book
# print("Please do not enter an empty string. \n\nIf you are finished, type "Done'.\n\nType 'List' to see the list of favourite books. \n")
# fav_book = ask_for_a_fav_book()
# elif fav_book =m"List":
# print(f"\nMy list of favourite books are: \n (list_of_favourite_books}")
# fav_book = ask_for_a_fav_book()
# elif check_list_for_book(fav_book):
# print(f"\n(fav_book) is one of my favourite books too.")
# fav_book = ask_for_a_fav_book()
# else:
# print("\nI haven't read that book.")
# print(f"\nI will add {fav_book} to my list.")
# add_a_book(fav_book)
# fav_book = ask_for_a_fav_book()