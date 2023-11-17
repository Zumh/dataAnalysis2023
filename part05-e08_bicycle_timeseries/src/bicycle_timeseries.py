#!/usr/bin/env python3



import pandas as pd

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
def split_date():
   
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')
  
     # cleaning all the missing values
    df = df.dropna(axis = 0, how='all').dropna(axis = 1, how='all')

    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)

    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    
    # drop Päivämäärä
    df = df.drop('Päivämäärä', axis=1) 
    
    df = pd.concat([d, df], axis=1)
    return df

def bicycle_timeseries():
    # read the data set from Helsingin bicycle time series data csv
    # cleans it 
  

    # first 5 column for date format
    date_format = split_date()

    # turn 5 date time columns into date time index Time Series.
    date_format["Date"] = pd.to_datetime(date_format[["Year", "Month", "Day", "Hour"]])
    # drop all the columns that we use for creating datetimeindex
    date_format = date_format.drop(columns=["Year", "Month", "Day", "Hour", "Weekday"], axis=1)
    DatetimeIndex = date_format.set_index(date_format["Date"])
    DatetimeIndex = DatetimeIndex.drop(columns=["Date"])
    return DatetimeIndex
 
def main():
    bicycle_timeseries()
    return None
if __name__ == "__main__":
    main()
