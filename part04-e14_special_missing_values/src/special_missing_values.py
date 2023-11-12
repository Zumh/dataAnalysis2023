#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():

    # read the file and transform in to data frame 

    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    df['LW'] = df['LW'].replace(['New', 'Re'], None)
    df['LW'] = pd.to_numeric(df['LW'], errors='coerce')
    return(df[df['Pos'] > df['LW']])
""" 
def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    m = (df["LW"] == "New") | (df["LW"] == "Re")
    df.loc[m, "LW"] = np.nan
    df["LW"] = pd.to_numeric(df["LW"])
    m2 = df["LW"] < df["Pos"]
    return df[m2]"""

def main():
    df = special_missing_values()
    print(df.shape ==  (17,7))
    return

if __name__ == "__main__":
    main()
