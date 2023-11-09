#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # return a1 = y and b1 = x -> y, x, z

    # d1 = a1*y + b1*x + c1 -> a1*y + b1*x - d1 =    -c1
    # d2 = a2*y + b2*x + c2 -> a2*y + b2*x - d2 =    -c2
    # d3 = a3*y + b3*x + c3 -> a3*y + b3*x - d3 =    -c3
    # -1 = -d1 from left equations constant value
    coeffecient = np.array([[ a1, b1, -1], [ a2, b2, -1], [ a3, b3, -1]])
    # Right-hand side values for the equations
    rhs = np.array([-c1, -c2, -c3])
    y, x, z = np.linalg.solve(coeffecient, rhs)
   
    return  x, y, z

""" 
def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    A=np.array([[-b1,-a1,1],[-b2,-a2,1], [-b3,-a3,1]])
    c=np.array([c1,c2,c3])
    sol = np.linalg.solve(A, c)
    return sol
"""

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1
    
    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
