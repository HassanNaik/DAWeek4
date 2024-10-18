# Libraries

# A libary is a collection of resources you can access when you need to.

# Everything we’ve been doing so far has been using the 
# Python standard or built-in library.
# This is the collection of objects, methods, modules, and 
# functions which make Python work as it does. 
# Python is a versatile language, and we’ve done a lot 
# with the built-in library already!

# When you installed Python, you also installed a number 
# of other Python libraries.
# They contain a lot of very useful bits of code that can 
# provide you with lots of functionality.

# These libraries can be quite specific –
# so Python limits your access to them. 
# You can only use them if you specifically want to.

# There are two ways we can import libraries – this way imports the 
# whole library, and we access all the methods with dot notation.

# We can just import the modules we need from a library. 
# When we do so, we don’t need to use dot notation anymore. 
# We just use the module name.

# Both are going to do the same thing.
# It’s generally better to just import what you need.

# Installing more 
# libraries - pip

# The built-in library and the list of importable libraries 
# give us a lot of functionality in Python. 
# You can also download more libraries and install them 
# using pip.

# Through pip, you can install more libraries. 
# You can install them globally – so you can always access them, 
# or locally so they’re unique to a project.

# The Python Package Index is a great online source for 
# Python libraries and packages.

# Would you like to add colour to your code?
# Let’s install colorama!

# In your terminal:
# pip install colorama
# A short install will take place.

# Folders, files, and scripts which are needed for a program to run are called dependencies.
# The program is dependent on that information.
# We have just installed Colorama to our own system.
# Behind the scenes, pip has installed it to the correct place with the 
# correct name to make it as easy as possible for me to use!

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)



print('back to normal now')

print("Hi")