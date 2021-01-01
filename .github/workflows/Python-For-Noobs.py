# Welcome to the Python For Noobs Guide!
# Here I will help newbies (no offense) with the basics.
# So yeah, let's get started!
# First up, print() Even pros might learn something here
import time # <-- Don't worry about this right now
print('Hello, this is text in a single quote!')
time.sleep(1) # <-- Don't worry about this either
# That last print thingamijig used single quotes.
# But you can also use double quotes
# I will mostly be using single, but you can use double
# Now time to break it down...
# It printed a string. That is text inside '' or inside "".
print("And this is text in a double quote!")
time.sleep(1)
# Just proving that you can use double quotes as well.
# Now, how to import things.
# Importing is like saying to python, "Hey, can you put all of this code
# in one line so I don't have to write all of it?" And python says, "Sure!"
# So now, a simple import thingamijig.
import math # With this, you have to do math.somerandomfunction()
from math import * # With this, you can just call the functions.
# Oh, I'm sorry, functions first. Functions are peices of code that you can
# reuse. Let me explain:
def MyFunction(): # Call the function something
    # The code
    print("Python is so fun and I love it!!!!")
    # End of code (unindent!!!)
# Unindented here
# Ok, now you might be thinking, Ok, how do I run this code
# that I made???????
# Simple:
MyFunction() # Parentheses following the function name.
# Pretty simple, right?
# Now what if we wanted to get user-inputted-text?
# Easy. Use the input() function,
time.sleep(1)
intro = input("Hello. Put text here: ") # and it would print "Hello.
# Put text here: *user puts text from keyboard here*"
# Notice I assigned it to a variable. Variables are something that you can reuse.
# So now, we can do this:
print(intro)
# Notice I didn't put quotes. That's not a mistake. I did that on purpose,
# and if I didn't, then it would print "intro". But, now it will print the
# text the user put in. If they put a space though, it would print " ", and
# look like nothing.
# So yeah, that is the basics. I hope you enjoyed!
