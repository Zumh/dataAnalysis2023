#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    
    # calculate the inner product 
    # we multiply the matrix and find the sum of the product
    euclidean_vector = np.sum(X * Y, axis = 1)

    # calculate the vector for X and Y
    vector_x = np.sqrt(np.sum(X**2, axis = 1))
    vector_y = np.sqrt(np.sum(Y**2, axis = 1))

    denomenator = vector_x * vector_y

    cos_radian = euclidean_vector/denomenator

    """
    Note: function np.arccos is only defined on the domain [-1.0,1.0]. 
    If you try to compute np.arccos(1.000000001), it will fail. 
    These kind of errors can occur due to use of finite precision in numerical computations. 
    Force the argument to be in the correct range (clip method).
    """
    cos_radian = np.clip(cos_radian, -1, 1)

    # transform this into arccos for degree
    acos = np.arccos(cos_radian)

    # then we find our degree using the formula for finding degree
    degree = (acos/(2 * np.pi)) * 360
    
    return np.array(degree)

def main():
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    a = vector_angles(A, B)
    result = a == [90, 90]
    print(result)

if __name__ == "__main__":
    main()
