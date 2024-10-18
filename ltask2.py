# Activity 2

# Using the list of quotes given (quotes.txt) create a program which
# allows a user to pick between seeing a random "Motivational","Fun", or "Meaningful" quote using a text input.

# A random quote from the corresponding list should appear.
# A motivational quote should be in blue.
# A fun quote should be in yellow.
# A meaningful quote should be in green.

# Users should not be able to submit a blank input.

# quotes.txt
# "Success is not final, failure is not fatal: It is the courage to continue that counts." – Winston Churchill
# "Don’t watch the clock; do what it does. Keep going." – Sam Levenson
# "The only way to do great work is to love what you do." – Steve Jobs
# "The harder you work for something, the greater you’ll feel when you achieve it." – Unknown
# "Believe you can and you're halfway there." – Theodore Roosevelt
# "Your limitation—it’s only your imagination." – Unknown
# "Success usually comes to those who are too busy to be looking for it." – Henry David Thoreau
# "It’s not about perfect. It’s about effort." – Jillian Michaels
# "Trying is the first step towards failure." – Homer Simpson
# "If something's hard to do, then it's not worth doing." – Homer Simpson
 
# "Life is short. Smile while you still have teeth." – Unknown
# "To live is the rarest thing in the world. Most people just exist." – Oscar Wilde
# "Laughter is timeless, imagination has no age, and dreams are forever." – Walt Disney
# "Do more things that make you forget to check your phone." – Unknown
# "Life is a great big canvas; throw all the paint you can on it." – Danny Kaye
# "A day without laughter is a day wasted." – Charlie Chaplin
# "The best way to cheer yourself up is to try to cheer somebody else up." – Mark Twain
# "Dance like no one is watching. Sing like no one is listening." – William W. Purkey
# "Every day may not be good, but there is something good in every day." – Unknown
# "The most wasted of all days is one without laughter." – E.E. Cummings
 
# "The unexamined life is not worth living." – Socrates
# "We are what we repeatedly do. Excellence, then, is not an act, but a habit." – Aristotle
# "In the middle of difficulty lies opportunity." – Albert Einstein
# "The only thing necessary for the triumph of evil is for good men to do nothing." – Edmund Burke
# "What lies behind us and what lies before us are tiny matters compared to what lies within us." – Ralph Waldo Emerson
# "Do not go where the path may lead, go instead where there is no path and leave a trail." – Ralph Waldo Emerson
# "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars." – Khalil Gibran
# "Life can only be understood backwards; but it must be lived forwards." – Søren Kierkegaard
# "We are not human beings having a spiritual experience. We are spiritual beings having a human experience." – Pierre Teilhard de Chardin
# "He who has a why to live can bear almost any how." – Friedrich Nietzsche




import random
# imports random libary
from colorama import Fore , Style #Back, 
# imports colour libary - commented Back as no longer being used.

fun_quotes = [
    "Life is short. Smile while you still have teeth. - Unknown",
    "To live is the rarest thing in the world. Most people just exist. - Oscar Wilde",
    "Laughter is timeless, imagination has no age, and dreams are forever. - Walt Disney",
    "Do more things that make you forget to check your phone. - Unknown",
    "Life is a great big canvas; throw all the paint you can on it. - Danny Kaye",
    "A day without laughter is a day wasted. - Charlie Chaplin",
    "The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain",
    "Dance like no one is watching. Sing like no one is listening. - William W. Purkey",
    "Every day may not be good, but there is something good in every day. - Unknown",
    "The most wasted of all days is one without laughter. - E.E. Cummings"
    ]
# created a list with list of quotes given in quotes.txt for fun
 
motivational_quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The harder you work for something, the greater you’ll feel when you achieve it. - Unknown",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your limitation—it’s only your imagination. – Unknown",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "It’s not about perfect. It’s about effort. – Jillian Michaels",
    "Trying is the first step towards failure. – Homer Simpson",
    "If something's hard to do, then it's not worth doing. – Homer Simpson"
    ]
# created a list with list of quotes given in quotes.txt for motivational

meaningful_quotes = [
    "The unexamined life is not worth living. – Socrates",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. – Aristotle",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "The only thing necessary for the triumph of evil is for good men to do nothing. – Edmund Burke",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars. – Khalil Gibran",
    "Life can only be understood backwards; but it must be lived forwards. – Søren Kierkegaard",
    "We are not human beings having a spiritual experience. We are spiritual beings having a human experience. – Pierre Teilhard de Chardin",
    "He who has a why to live can bear almost any how. – Friedrich Nietzsche"
    ]
# created a list with list of quotes given in quotes.txt for meaningful
 
category = input("Enter 1 for Fun, 2 for Motivational, 3 for Meaningful: ")
# user will enter a number 

while category not in ["1", "2", "3"]:
    print(Fore.RED + "Invalid input! Please enter 1, 2 or 3.")
    print(Style.RESET_ALL)
    category = input("Enter 1 for Fun, 2 for Motivational, 3 for Meaningful: ")

# creates a while loop until user inputs 1,2 or 3
# tested by entering 0,4,8,,9,10,14,100,1000 it returned "Invalid input! Please enter 1, 2, or 3" in red
# tested user input 1,2,3

# while category >= "3" or category == "0" or category >="10" or category =="10":
#     print(Fore.RED + "Invalid input! Please enter 1, 2, or 3.")
#     print(Style.RESET_ALL)
#     category = input("Enter 1 for Fun, 2 for Motivational, 3 for Meaningful: ")

# while category == "0":
#     print(Fore.RED + "Invalid input! Please enter 1, 2, or 3.")
#     print(Style.RESET_ALL)
#     category = input("Enter 1 for Fun, 2 for Motivational, 3 for Meaningful: ")

# line 111 to 119 commented out as i added new while loop category not in ["1", "2", "3"]:

if category == "1":
    quote = random.choice(fun_quotes)
# takes user input 1 and returns a random quote for list fun_quotes
    print(Fore.YELLOW + quote)
# A fun quote should be in yellow.
    print(Style.RESET_ALL)
# changes the text back to the original

if category == "2":
    quote = random.choice(motivational_quotes)
# takes user input 2 and returns a random quote for list motivational_quotes
    print(Fore.BLUE + quote)
# A motivational quote should be in blue.
    print(Style.RESET_ALL)
# changes the text back to the original

if category == "3":
    quote = random.choice(meaningful_quotes)
# takes user input 3 and returns a random quote for list meaningful_quotes
    print(Fore.GREEN + quote)
# A meaningful quote should be in green.
    print(Style.RESET_ALL)
# changes the text back to the original

