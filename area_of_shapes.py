#!/usr/bin/python3
import math

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        shape_type = area_rectangle()

    elif shape == "circle":
        shape_type = area_circle()

    else:
        print("Please enter a rectangle or a circle ! ")
        
def area_rectangle():
    length = float(input("Enter the length of your rectangle: "))
    width = float (input("Enter the width of your rectangle: "))
    area = length * width
    print("The area of the rectangle is {}".format(area))

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * math.pow(radius, 2)
    print("The area of a circle is {:.2f}".format(area))


def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)

main()
