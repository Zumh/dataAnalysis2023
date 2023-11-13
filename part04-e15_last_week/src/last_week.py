#!/usr/bin/env python3

import pandas as pd
import numpy as np
def last_week():
    # The function should then try to reconstruct the top40 list of the previous week based on that week's list
    
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')    
     
    # WoC means "Weeks on Chart", that is, on how many weeks this song has been on the top 40 list.
    # previous week -> so we have to take a way one week
    df["WoC"] -= 1
    # last week top 40 were on last week list
    week_mask = df['WoC'] > 1
    top40 = df.where(week_mask).dropna()

    # convert all the last week position to numeric value
    top40['LW'] = pd.to_numeric(top40['LW'], errors='coerce')

    # create a mask for filtering out Peak position that are not valid for previous/last week
    drop_pos_mask = (top40['Peak Pos'] == top40['Pos']) & (top40['Pos'] < top40['LW'])
    top40.loc[drop_pos_mask, 'Peak Pos'] = np.nan 
    
    
    # sort with last week position
    top40.sort_values(by=['LW'])
    
    # change the index using last week position
    # a new organize index position same as last week or previous week
    top40.index = top40['LW']
    # we have to make to 40 rank positions
    top40 = top40.reindex(range(1, len(df) + 1))

    # get rid off last week positions after we done using it
    top40['LW'] = np.nan
    
    # get a new current positions 
    top40['Pos'] = top40.index
    
    return(top40)



def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
