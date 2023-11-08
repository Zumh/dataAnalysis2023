#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    """
    The function should return a new array containing those rows 
    from the input that have the value in the second column larger than
    in the second last column.
    """
    second_column = a[:,1]
    second_last_column = a[:,-2]

    larger_than_bool = (second_column > second_last_column)
    larger_than_rows = a[larger_than_bool]
   
    return larger_than_rows
    
def main():
    matrix = np.array([[8, 9, 3, 8, 8],
                  [0, 5, 3, 9, 9],
                  [5, 7, 6, 0, 4],
                  [7, 8, 1, 6, 2],
                  [2, 1, 3, 5, 8]])
    result=column_comparison(matrix)
    print(result)

if __name__ == "__main__":
    main()
