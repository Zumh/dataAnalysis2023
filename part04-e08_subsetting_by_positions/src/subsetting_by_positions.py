#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions():
    #return pd.DataFrame()
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    # top 10 with Title and Artist
    return (df.iloc[0:10, [2,3]])
 

def main():
    result = subsetting_by_positions()
    print(result)

if __name__ == "__main__":
    main()
