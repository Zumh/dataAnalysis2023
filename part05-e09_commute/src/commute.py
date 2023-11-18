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

def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)

    ## no need to concatenate, it completely ignore weekday column here 
    df["Date"] = pd.to_datetime(d[["Year", "Month", "Day", "Hour"]]) 
    # it drop the Päivämäärä column and set index date
    df = df.drop("Päivämäärä", axis=1)
    df = df.set_index("Date")
    return df

def commute():
    time_series = bicycle_timeseries()
    
    # REstrict to August 2017, group by the weekday, aggregate by summing.
    time_series = time_series['2017-8-1':'2017-8-31']
    restrict_date = time_series.groupby(time_series.index.weekday).sum()
    # Set the Weekday column to numbers from one to seven. Then set the column Weekday as the (row) index.
    restrict_date['Weekday'] = range(1, 8)
    #print(restrict_date.index.weekday)
    restrict_date = restrict_date.set_index('Weekday')
    return (restrict_date)

 
    
def main():
    df = commute()
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.plot(df)
    plt.gca().set_xticklabels(weekdays)
    
    plt.show()


if __name__ == "__main__":
    main()
