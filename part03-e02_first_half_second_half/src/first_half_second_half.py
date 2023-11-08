#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    n, m = a.shape
    mid = m//2
    first_half = np.sum(a[:, :mid], axis = 1)
    last_half = np.sum(a[:, mid:], axis = 1)

    first_half_larger_row = a[(first_half > last_half)]
    return (first_half_larger_row)


def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
    first_half_second_half(a)

if __name__ == "__main__":
    main()
