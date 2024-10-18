# Activity 1
# Create a function which takes input of a user’s name as 
# a parameter and prints the happy birthday song to 
# them.

# Happy Birthday to you
# Happy Birthday to you
# Happy Birthday dear (name)
# Happy Birthday to you.

name = input("Whos birthday is it? ").title()
a = "Happy Birthday to you,"
b = "Happy Birthday dear "

def birthday_song(name):
    print(a)
    print(a)
    print(f"{b}{name}")
    print("hi {}".format(name))
    print(a)

birthday_song(name)
