# Activity 1
# Create a program which calculates how many days you’ve been alive for.
# Hints: Look into the datetime library, and don’t use 
# input!

import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x)

birthdate = datetime.date(1989, 4, 5)  
 
today = datetime.date.today()
 
days_alive = (today - birthdate).days
 
print(f"You have been alive for {days_alive} days!")