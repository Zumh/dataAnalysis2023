#!/usr/bin/env python3

import numpy as np

def diamond(n):
    # eye and concatenate
    # NumPy and array slicing

    # create an eye
    top_half = np.eye(n, dtype = int)
 
  
    # flip and remove the first row
    # bottom_half = np.flip(top_half, axis = 0)[1:]

    # we flip the top half to make it bottom
    bottom_half = top_half[::-1,:]

    # we remove the first row of the bottom
    bottom_half = bottom_half[1:,:]
  
    # right side 
    # we concatenate top half and bottom half to make it the right side of the diamond
    right_side = np.concatenate((top_half, bottom_half))
    
    #left_side = np.flip(right_side, axis = 1)[:,:-1]

    # flip the right side of the diamond to make it left
    left_side = right_side[:,::-1]
    
    # then we remove the last column of the left side
    left_side = left_side[:,:-1]

    # diamond = concatenate left side and right side column or horizontal wise
    diamond = np.concatenate((left_side, right_side), axis = 1)
    return(diamond)
def main():
    result = diamond(1)
    print(result)
if __name__ == "__main__":
    main()
