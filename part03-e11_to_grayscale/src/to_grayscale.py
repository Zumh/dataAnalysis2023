#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_red(image_array):
    # zeroes out green, blue
    image_array[:, :, [1,2]] = 0

    return image_array

def to_green(image_array):
    # zeroes out red, blue
    image_array[:, :, [0,2]] = 0
    return image_array
    
def to_blue(image_array):
    # zeroes out green, red
    image_array[:, :, [ 0, 1]] = 0
    return image_array

def to_grayscale(image_array):
    # gray_scale image
    # red, green, blue is weight sum that transform into grayscale image
    gray_image = 0.2126 * image_array[:, :, 0] + 0.7152 * image_array[:, :, 1] + 0.0722 * image_array[:, :, 2]

    return gray_image
def main():
    image_array = plt.imread("src/painting.png")
    gray_image = to_grayscale(image_array)
    plt.gray()
    plt.imshow(gray_image)

    # top red, middle green, bottom blue
    row, column = 3, 1
    fig, ax = plt.subplots(row, column)
    red_image = image_array.copy()
    red_image = to_red(red_image)
    ax[0].imshow(red_image) # top row red image
    green_image = image_array.copy()
    ax[1].imshow(to_green(green_image)) # middle row green image
    blue_image = image_array.copy()
    ax[2].imshow(to_blue(blue_image)) # bottom row blue image
    plt.show()


if __name__ == "__main__":
    main()
