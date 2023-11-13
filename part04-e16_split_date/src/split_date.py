#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')

    week_days = { 'ma' : 'Mon',
    'ti' : 'Tue',
    'ke' : 'Wed',
    'to' : 'Thu',
    'pe' : 'Fri',
    'la' : 'Sat',
    'su' : 'Sun'}

    months = {'tammi': 1,
    'helmi': 2,
    'maalis': 3,
    'huhti': 4,
    'touko': 5,
    'kesä': 6,
    'heinä': 7,
    'elo': 8,
    'syys': 9,
    'loka': 10,
    'marras': 11,
    'joulu': 12}

    column_names = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    # clean up all the nan from columns and rows that are fully NaN
    clean_df = df.dropna(axis = 0, how='all').dropna(axis = 1, how='all')
    
    # Then split the Päivämäärä column into a DataFrame with 
    # five columns with column names Weekday, Day, Month, Year, and Hour.
    split_date = clean_df['Päivämäärä'].str.split(expand=True)

    # change columns s
    split_date.columns = column_names

    # change we days with matching key
    # isolate the weekday and change their format
    split_date['Weekday'] = split_date['Weekday'].map(week_days)
    split_date['Day'] = split_date['Day'].astype(int)
    split_date['Month'] = split_date['Month'].map(months).astype(int)  
    split_date['Year'] = split_date['Year'].astype(int)
    split_date['Hour'] =split_date['Hour'].str[:2].astype(int)

    return split_date

def main():
    result = split_date()
    return result
if __name__ == "__main__":
    main()
