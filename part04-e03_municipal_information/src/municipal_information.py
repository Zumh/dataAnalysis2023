#!/usr/bin/env python3

import pandas as pd

def main():
    # seperator is tabulator \t
    data_frame = pd.read_csv("src/municipal.tsv", sep='\t')
    #print(data_frame.head()) # print the first five rows
    r, c = data_frame.shape

    print(f"Shape: {r},{c}")
    print("Columns:")
    for col in data_frame.columns.tolist():
        print(col)


if __name__ == "__main__":
    main()
