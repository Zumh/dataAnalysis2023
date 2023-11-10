#!/usr/bin/env python3

import pandas as pd



def read_series():
    #datas=["a  12", "b	 3", "c	50", "ere"]
    datas = []
    while True:
        user_input = input("input key and value: ")
        if user_input == "":
            break
        datas.append(user_input.strip())
        
    try:
        # split the data using white space
        split_data = [data.split() for data in datas]
        return pd.Series(dict(split_data))
    except TypeError:
        pass

     
    return pd.Series([])
"""
# model solution
def read_series():
    values=[]
    indices=[]
    while True:
        line = input("")
        if not line:
            break
        i, v = line.split()
        values.append(v)
        indices.append(i)
    s = pd.Series(values, index=indices)
    return s
"""
def main():
    pass

if __name__ == "__main__":
    main()
