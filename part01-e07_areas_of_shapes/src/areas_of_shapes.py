#!/usr/bin/env python3

import math

def triangle_area(base, height):
    return (base * height) * (1/2)

def rectangle_area(length, height):
    return length * height;

def circle_area(radius):
    import math 
    return math.pi * (radius ** 2)

def main():
    # enter you solution here
    area = 0
    while True :
        user_input = input("Choose a shape (triangle, rectangle, circle): ")
        area = 0
        if user_input == "":
            break
        elif user_input == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = triangle_area(base, height)
        elif user_input == "rectangle":
            length = float(input("Give width of the rectangle: "))
            width = float(input("Give height of the rectangle: "))
            area = rectangle_area(length, width)
        elif user_input == "circle":
            radius = float(input("Give radius of the circle: "))
            area = circle_area(radius)
        else:    
            print("Unknown shape!")
        if area > 0:
            print(f"The area is {area:.6f}")   
if __name__ == "__main__":
    main()
