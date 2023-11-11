#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    # returns the proportion of municipalities with increasing population in that subset.
    # check change of population from above 0
    increasing_pop = df[df["Population change from the previous year, %"]>0]
    value = (len(increasing_pop) / len(df))
    return value

def main():
    path = "src/municipal.tsv"
    df = pd.read_csv(path, sep='\t', index_col='Region 2018')
    # extract manuciplities of findland 'Akaa':'Äänekoski'
    findland_manucipal = df['Akaa':'Äänekoski']

    
    growing_proportion = growing_municipalities(findland_manucipal)
    print(f"Proportion of growing municipalities: {growing_proportion:.1f}%")

if __name__ == "__main__":
    main()
