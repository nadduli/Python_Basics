#!/usr/bin/python3
""" solve the equation x + 4 = 9 using a function
"""

def eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)
print(eq("x + 4 = 9"))
