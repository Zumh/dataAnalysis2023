#!/usr/bin/env python3

from functools import reduce 
import numpy as np


def matrix_power(a, n):

    _, m = a.shape

    # if n is zer0 return identity matrix
    if n == 0:
        return np.eye(m)
    elif n < 0: 
        # if it is negative power we trying to get the identity of matris       
        return np.linalg.inv(matrix_power(a, -n))
    elif n == 1:
        return a
    
    result  = reduce(lambda x, _: x @ a, range(n-1), a)
    return result

def main():
    a = np.array([[1,2], [3,4]])
    result = matrix_power(a, 0)
    print(a)
    print(result)

if __name__ == "__main__":
    main()
