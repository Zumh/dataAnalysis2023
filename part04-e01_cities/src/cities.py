#!/usr/bin/env python3

import pandas as pd

def cities():
    indicies = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    datas = [
        [643272, 715.48],
        [279044, 528.03],
        [231853, 689.59],
        [223027, 240.35],
        [201810, 3817.52]
        ]
    return pd.DataFrame(datas, columns=["Population", "Total area"],index=indicies)
   
    
def main():
    df = cities()
    cols=df.columns
    ind=df.index
    print(cols)
    print(ind)
    print(df)
    return
main()
    
if __name__ == "__main__":
    main()
