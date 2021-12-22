#!/usr/bin/python3

""" get a string from a user
   - convert the string to uppercase
   - convert the string into a list
   - cycle through the list and get the first character
   - remove the newline and later add a newline
"""

words = input('Enter the string: ')
words = words.upper()
word = words.split()

for i in word:
    print(i[0], end="")
print()
