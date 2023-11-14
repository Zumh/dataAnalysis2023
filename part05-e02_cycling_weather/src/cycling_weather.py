#!/usr/bin/env python3

import pandas as pd


days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
def split_date(df):
   
    
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)

    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d


def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')

    # cleaning all the missing values
    df = df.dropna(axis = 0, how='all').dropna(axis = 1, how='all')

    # first 5 column for date format
    date_format = split_date(df)
    
    # drop Päivämäärä
    df = df.drop('Päivämäärä', axis=1) 
   
    
    # rest 20 concerning the measurment location
    df = pd.concat([date_format, df], axis=1)

    return df


def cycling_weather():
    
    cycling_data_set = split_date_continues()
    weather_data_set = pd.read_csv("src/kumpula-weather-2017.csv", sep=',')
     
    merge_data = pd.merge(cycling_data_set, weather_data_set, left_on=['Year','Month','Day'], right_on=['Year','m','d'])
    drop_columns = ['m','d','Time','Time zone']
   
    merge_data = merge_data.drop(columns=drop_columns)

    return merge_data

   

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
