#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland(path):
    data_frames = pd.read_csv(path, sep='\t', index_col='Region 2018')
    # extract manuciplities of findland 'Akaa':'Äänekoski'
    findland_manucipal = data_frames['Akaa':'Äänekoski']
    return findland_manucipal

def swedish_and_foreigners():
    path = "src/municipal.tsv"

    df = municipalities_of_finland(path)

    # Swedish speaking people and 
    # proportion of foreigners both above 5 % level
    swedish_speaking_percent = "Share of Swedish-speakers of the population, %"
    foreign_citizens_percent = "Share of foreign citizens of the population, %"
    percent = 5
    condition = (df[swedish_speaking_percent] > percent) & (df[foreign_citizens_percent] > percent)
    five_percent = df[condition]

    return (five_percent[["Population",swedish_speaking_percent,foreign_citizens_percent]])

def main():
    result = swedish_and_foreigners()
    print(result)

if __name__ == "__main__":
    main()
