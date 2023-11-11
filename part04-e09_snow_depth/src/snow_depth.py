#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    """returns the maximum amount of snow in the year 2017."""
    # read csv file and calculate the satistics
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=',')
    snow_amount = 'Snow depth (cm)'
  
    # extract rows from year 2017
    target_year = df[df.loc[:, "Year"] == 2017]
    max_snow_amount = max(target_year.loc[:,snow_amount])
    
    return max_snow_amount

def main():
    result = snow_depth()
    print(f"Max snow depth: {result:.1f}")

if __name__ == "__main__":
    main()
