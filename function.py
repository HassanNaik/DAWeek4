#Functions, Python function is a block of code, that runs only when it is called. 
# It is programmed to return the specific task.

# Functions allow us to break our code up into small, reusable chunks. 
# When we need to use the function, we use its name.You’ve already been using them!

# print() len() input() lower()
# are all built-in functions! 
# Someone else has already written the jobs those functions do, and we just use them when we need to!
# Note – a method (like .lower()) is a function that only works on a specific object.

#List of functions:

# abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	Returns the binary version of a number
# bool()	Returns the boolean value of the specified object
# bytearray()	Returns an array of bytes
# bytes()	Returns a bytes object
# callable()	Returns True if the specified object is callable, otherwise False
# chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method
# compile()	Returns the specified source as an object, ready to be executed
# complex()	Returns a complex number
# delattr()	Deletes the specified attribute (property or method) from the specified object
# dict()	Returns a dictionary (Array)
# dir()	Returns a list of the specified object's properties and methods
# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	Evaluates and executes an expression
# exec()	Executes the specified code (or object)
# filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
# format()	Formats a specified value
# frozenset()	Returns a frozenset object
# getattr()	Returns the value of the specified attribute (property or method)
# globals()	Returns the current global symbol table as a dictionary
# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system
# hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# issubclass()	Returns True if a specified class is a subclass of a specified object
# iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
# max()	Returns the largest item in an iterable
# memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable
# object()	Returns a new object
# oct()	Converts a number into an octal
# open()	Opens a file and returns a file object
# ord()	Convert an integer representing the Unicode of the specified character
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device
# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	Returns a readable version of an object
# reversed()	Returns a reversed iterator
# round()	Rounds a numbers
# set()	Returns a new set object
# setattr()	Sets an attribute (property/method) of an object
# slice()	Returns a slice object
# sorted()	Returns a sorted list
# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators

# Some functions don’t need any specific information from us to work –they just do their job.
# Others might expect information from us to work with - it might have parameters. 
# We fill in the spaces of the parameters with arguments.

# Defining Your Own Functions

# Function syntax

# This is the syntax used in Python when you’re creating your own function.

# def is the keyword needed to let Python know you will be defining a new function.

# def s_h():
#     print("hello")
# s_h()

# Parameters

# Functions are great if you’re going to be repeating a process but with different data. 
# The job of a function is to take data and process it.
# When we defined our function in this example, we also told it to expect some information. 
# We told it how to work with this information without knowing exactly what it is, a bit like a variable! 
# This is a parameter.

# When we call the function, we need to supply that instance of the function call with the information we want it to work with. 
# This is an argument.

# This gives our function a lot more use cases! 
# It’s more flexible and can be used in many more situations.

# Digging deeper -Scope

# Variable scope refers to the region of the code where we can access variables. 
# We’ll be looking at the two main Python scopes –global and local.

def s_t(st):
    print(f"{st}")
s_t("HI")
s_t("How are you")
s_t("Bye")
s_t(2)
s_t(2 + 2)

def s_h():
    print("hello")
s_h()

def s_g():
    print("Good Bye")
s_g()

def cash_withdrawal(amount,accnum):
    amount = input("how much? ")
    accnum = input("from? ")
    print(f"You are withdrawing £{amount} from account: {accnum}")

cash_withdrawal(50, 12345678)
cash_withdrawal(100, 87654321)
cash_withdrawal(200, 19876534)

#cash_withdrawal(input("How much are you withdrawing?"), input("From which account?"))

def o(size, type):
    print(f"I'd like a {size} {type} please" )

o(input("What Size? "), input("What drink? "))


