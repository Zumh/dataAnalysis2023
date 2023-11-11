#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    data_frame = pd.read_csv("src/municipal.tsv", sep='\t', index_col='Region 2018')
   
    #return data_frame.loc['Akaa':'Äänekoski']
    return data_frame['Akaa':'Äänekoski']
    
def main():
    municipalities_of_finland()
    
if __name__ == "__main__":
    main()
