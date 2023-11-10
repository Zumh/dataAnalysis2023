#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
def center(a):
    # returns coordinate pair (center_y, center_x) of the image center.
    # find the length of width and height and cut them in the middle
    # work for 2D and 3D
    height, width = a.shape[0], a.shape[1]

    # we sub tract 1 because from height because array start at 0 
    return (height-1)/2.0, (width-1)/2.0     # note the order: (center_y, center_x)
"""
def radial_distance(a):
    return np.array([[]])
"""
def eucldian_distance(x, y, center_x, center_y):
    return np.sqrt((x - center_x)**2 + (y - center_y)**2)
def radial_distance(a):
    """
    for image with width w and height h an array with shape (h,w), 
    where the number at index (i,j) 
    gives the euclidean distance from the point (i,j) to the center of the image.
    
    The distance is calculated as:

    sqrt((x - center_x)^2 + (y - center_y)^2)

    """
    center_x, center_y = center(a)
    radial = []
    height, width, _ = a.shape

    for i in range(height):
        for j in range(width):
            
            current = eucldian_distance(j, i, center_x, center_y)
            radial.append(current)
    return np.array(radial).reshape((height, width))

def scale(a, tmin=0.0, tmax=1.0):
    """
    Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax].
    we going to use linear interpolation 
    from current max and min value to desire range between tmin, tmax for each element
    linear interpolation will calculate and fill values between scaled a's element or points
    """
    # np.interp(image_array_value, (current min , current max), (desire min, desire max))
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    # returns an array with same height and width
    # filled with values between 0.0 and 1.0
    """
    To make the resulting array values near the center of array to be close to 1 and 
    closer to the edges of the array are values closer to be 0
    # this inturn will make the center portion brighter and closer to the edge darker
    radial_distance calculate the distance to cover and scale
    scaling function or linear interpolation made this smoother transition.
    """
    # we are subtracting previous array from 1 
    return np.round(scale(1 - radial_distance(a)))

def radial_fade(a):
    """
    radia_mask(a) return array
        Original array:
        [[1 2 3]
        [4 5 6]
        [7 8 9]]
        get a new axis using np.newaxis to match with original image dimension a
        Modified array:
        [[3]
        [6]
        [9]
        [2]
        [5]
        [8]
        [1]
        [4]
        [7]]
    a * (radial_mask reshape) -> we mask the original image
    """
    return a * radial_mask(a)[:,:,np.newaxis]
 

def main():
    image_array = plt.imread("src/painting.png")
    """
    op the original painting.png, 
    in the middle the mask, and 
    on the bottom the faded image.
    """

    plt.subplot(3, 1, 1)
    plt.imshow(image_array)
    plt.subplot(3, 1, 2)
    plt.imshow(radial_mask(image_array))
    plt.subplot(3, 1, 3)
    plt.imshow(radial_fade(image_array))
    plt.show()

if __name__ == "__main__":
    main()
