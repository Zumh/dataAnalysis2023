#!/usr/bin/env python3

import pandas as pd


def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')
    # Example DataFrame
    dropw_column = df.dropna(axis = 1, how='all')
    drop_row = dropw_column.dropna(axis = 0, how='all')
    return(drop_row)


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
