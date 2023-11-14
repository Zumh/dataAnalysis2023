#!/usr/bin/env python3

import pandas as pd

def top_bands():
    # top40UK
    top40UK = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    bands = pd.read_csv("src/bands.tsv", sep='\t')
    bands['Band'] = bands['Band'].str.title()
    top40UK['Artist'] =  top40UK['Artist'].str.title()
  
    merge_data = pd.merge(top40UK, bands, left_on='Artist', right_on='Band')
   
    return merge_data

def main():
    top_bands()

if __name__ == "__main__":
    main()
