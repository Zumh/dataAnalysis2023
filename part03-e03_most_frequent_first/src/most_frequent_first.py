#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    base_column = a[:,c]
    # sort rows base on most frequent true value
    unique_values, count_number = np.unique(base_column, return_counts=True)
    
    # map the frequency of number to each unique values
    frequency = dict(zip(unique_values, count_number))
    
    # map base_column with frequency table in descending order 
    base_column_frequency = [-frequency[value] for value in base_column]

    # extract sorted indecies from the base_column_frequency
    sorted_frequency_indecies = np.argsort(base_column_frequency)
    
    # use that sorted indecies to sort the rows of original matrix -> a
    return a[sorted_frequency_indecies]

def main():
    data = [
        [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
        [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
        [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
        [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
        [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
        [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
        [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
        [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
        [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
        [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]
    ]

    numpy_array = np.array(data)
    sorted_matrix = most_frequent_first(numpy_array, -1)
    print(sorted_matrix)

if __name__ == "__main__":
    main()
