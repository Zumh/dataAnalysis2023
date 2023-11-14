#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    # top40UK
    who_suicide_stats = pd.read_csv("src/who_suicide_statistics.csv", sep=',')

    # the mean fraction of suicides per population in that country
    who_suicide_stats['suicide_fraction'] = who_suicide_stats['suicides_no']/ who_suicide_stats['population']

    average_suicide = who_suicide_stats.groupby('country')['suicide_fraction'].mean()
    
    return (average_suicide)
 

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
