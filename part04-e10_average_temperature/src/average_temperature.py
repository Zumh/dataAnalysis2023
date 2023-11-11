#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    """returns the average temperature in July."""
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=',')
    month = 7
    target_month = df[df.loc[:, 'm'] == month]
    temperature = target_month['Air temperature (degC)']
    return sum(temperature)/len(temperature)

def main():
    avg = average_temperature()
    print(f"Average temperature in July: {avg:.1f}")

if __name__ == "__main__":
    main()
