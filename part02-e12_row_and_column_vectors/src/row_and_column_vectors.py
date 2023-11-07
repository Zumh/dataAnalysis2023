#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    n, m = a.shape
    # Use np.split to split the matrix a long axis 0 ( rows )
    row_vectors = np.split(a, n)

    return row_vectors

def get_column_vectors(a):
    n, m = a.shape
    # Use np.split to split the matrix a long axis 0 ( rows )
    column_vectors = np.split(a, m, axis = 1)
    return column_vectors

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
