#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
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
def cyclists_per_day():
   
    # first 5 column for date format
    date_format = split_date_continues()
    
    # Group the rows by year, month, and day. 
    group_columns = ["Year","Month","Day"]
    drop_group = ['Weekday', 'Hour']
    # Get the sum for each group Year, Month, and Day
    group_data = date_format.drop(columns=drop_group)
    group_data = group_data.groupby(group_columns).sum()
    
    
    return group_data
    
def main():
    daily_counts = cyclists_per_day()
    specifici_month_cyclists = daily_counts.loc[(2017, 9),:]
   
   
    plt.plot(specifici_month_cyclists)
    plt.xticks(range(1, 32))
    plt.title("August of year 2017")  # Add a title to the figure
    plt.xlabel("Days")       # Give a label to the x-axis
    plt.ylabel("Cyclists")       # Give a label to the y-axis
    plt.show()  
 

if __name__ == "__main__":
    main()
