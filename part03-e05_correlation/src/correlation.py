#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values
    #return pd.read_csv("iris.csv").drop('species', axis=1).values

def lengths():
    # What is the Pearson correlation between the variables sepal length and petal length
    data = load()
    sepal_length, petal_length = data[:,0], data[:,2]
    length_correlation = scipy.stats.pearsonr(sepal_length, petal_length)[0]

    return length_correlation

def correlations():
    data = load()
    
    result = np.corrcoef(data,  rowvar=False)
    
    return result

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
