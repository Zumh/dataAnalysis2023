#!/usr/bin/env python3



import pandas as pd
import numpy as np
def powers_of_series(s, k):

    
    # create pd dataframes here 
    data = pd.DataFrame(s, columns=[1])
    

    for number in range(1, k+1):
      
        data[number] = data[1] ** number

    return data
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    k = 3
    df = powers_of_series(s, k)
    print(df)
    
if __name__ == "__main__":
    main()
