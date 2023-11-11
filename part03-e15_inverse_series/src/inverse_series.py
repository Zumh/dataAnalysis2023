#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    """
        Write function inverse_series that get a Series as a parameter and 
        returns a new series, whose indices and values have swapped roles. 
        Test your function from the main function.
    """

    
    return pd.Series(s.index, s.values)

def main():
    L=[1,2,3,1]
    ind=list("abcd")
    s = pd.Series(L, index=ind)
    print(s)
    t = inverse_series(s)
    print(t)

if __name__ == "__main__":
    main()
