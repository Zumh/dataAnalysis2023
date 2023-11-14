#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    # top40UK
    top40UK = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    print(top40UK.shape)

    # here we going to group by WoC and sum
    publisher_stats = top40UK.groupby('Publisher')['WoC'].sum()
    
 
    # find the best publisher by maximum WoC sum. 
    # it return the index or key of maximum value from pandas series
    best_pubisher = publisher_stats.idxmax()

    # now we extract data frame of the best publisher from the original top40UK
    best_pubisher_record = top40UK[top40UK['Publisher'] == best_pubisher]
 
    return best_pubisher_record

def main():
    best_record_company()


if __name__ == "__main__":
    main()
