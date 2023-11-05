# Enter you module contents here
"""
This file is for calculating triangle's hypotenous and area.
"""
import math

__version__ = "1"
__author__ = "John snow"
def hypotenuse(a, b):
    """
    Calculate hypotenuse of a triangle

    Parameters:
    param1 (int): a side
    param2 (int): b side

    Returns:
    float: c 
    """
    return math.sqrt(a**2 + b**2)

def area(base, height):
    """
    Calculate area of a triangle

    Parameters:
    param1 (int): base 
    param2 (int): height 

    Returns:
    float: area 
    """
    return (base * height)/2