#!/usr/bin/env python3

import numpy as np
#import scipy.linalg


def vector_lengths(a):
    # return an array of shape (n,)
    # that has the length of each vector in the input. 
    # Euclid norm for ||V|| = sqrt(3^2 + 4^2)
    # use vectorized operations. 
    # the np.sum and the np.sqrt functions. 
    
    # square
    value  = a**2
    value = value.sum(axis=1)
    value = np.sqrt(value)


  

    return np.array(value)


def main():
    n=10
    for m in range(1,5):
        a=np.random.randn(n, m)
        result = vector_lengths(a)
        if result.shape == (n,):
            print(f"{result.shape}")

if __name__ == "__main__":
    main()
