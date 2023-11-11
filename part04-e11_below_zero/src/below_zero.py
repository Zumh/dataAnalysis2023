#!/usr/bin/env python3

import pandas as pd


def below_zero():
    """returns the number of days when the temperature was below zero."""
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=',')
    number_of_days = 0
    temperature = df[df['Air temperature (degC)'] < 0] 
    return len(temperature)

def main():
    result = below_zero()
    print(f"Number of days below zero: {result:02d}")
    
if __name__ == "__main__":
    main()
