#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    indecies = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]

    presidents = [np.nan, 'Niinistö', 'Trump', np.nan, 'Steinmeier', 'Putin']
    years = [np.nan, 1917, 1776, 1523, np.nan, 1992]
    datas = {
        'Year of independence':years,
        'President':presidents
    }
  
    result = pd.DataFrame(datas, index=indecies)
  
  

    return(result)
               
def main():
    result = missing_value_types()
    print(result)

if __name__ == "__main__":
    main()
