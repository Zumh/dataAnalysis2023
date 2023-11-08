#!/usr/bin/python3

import numpy as np

# y = mx + b
 
def meeting_lines(a1, b1, a2, b2):
    # make coeffient for two lines
    # line1 coefficient-> a1x -y = -b1
    # line2 coefficient-> a2x -y = -b2
    line1 = np.array([[a1, -1],[a2, -1]])
    line2 = np.array([-b1, -b2])

    # then we can calculate intersection point
    x, y = np.linalg.solve(line1, line2)
    
    return x, y

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
