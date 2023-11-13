#!/usr/bin/env python3

import pandas as pd
import numpy as np


def modified_names(df):
    result = (
        df
        .apply(
            lambda name: 
                ' '.join(
                        reversed([part for part in name.split(',')])
                    ).strip().title()
                
        )
        
    )
    return result 

def cleaning_data():
    # The columns should have dtypes object, integer, float, integer, object.
    df= pd.read_csv("src/presidents.tsv", sep='\t')
    word_to_number = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
    President, Start, Last, Seasons, Vice_president = df.columns
    # Clean up names
    df[President] = modified_names(df[President]).astype(str)
    df[Vice_president] = modified_names(df[Vice_president]).astype(str)

    # Clean up start and last
    df[Last] =  pd.to_numeric(df[Last], errors='coerce')
    df[Start] = df[Start].str.split().apply(lambda year: year[0]).astype(int)

    df[Seasons] = df[Seasons].map(lambda x: int(x) if str(x).isdigit() else word_to_number.get(x, x))
    return df

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
