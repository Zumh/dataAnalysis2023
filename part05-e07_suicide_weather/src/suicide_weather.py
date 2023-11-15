#!/usr/bin/env python3

import pandas as pd

# Copy the function suicide fractions from the previous exercise. 
def suicide_fractions():
 
    who_suicide_stats = pd.read_csv("src/who_suicide_statistics.csv", sep=',')

    # the mean fraction of suicides per population in that country
    who_suicide_stats['suicide_fraction'] = who_suicide_stats['suicides_no']/ who_suicide_stats['population']

    average_suicide = who_suicide_stats.groupby('country')['suicide_fraction'].mean()

    return(average_suicide)


    
def suicide_weather():
    
    
    path = 'src/List_of_countries_by_average_yearly_temperature.html'
    average_suicide = suicide_fractions()
    suicide_rows = len(average_suicide)
    # Set the first column as the index and use the first row as the header
    # extract the csv 
    weather_data = pd.read_html(path, index_col=0, header=0)[0]
    # we explicitly convert unicode minus sign to normal minus sign, it works
    temperature = weather_data.replace(r'[^0-9.-]', '-', regex=True)
    temperature_rows = len(temperature)
    
    # convert it to float number
    temperature['Average yearly temperature (1961–1990, degrees Celsius)'] = pd.to_numeric(temperature['Average yearly temperature (1961–1990, degrees Celsius)'])

    # once we merge together the table have same dimension 
    common = pd.merge(average_suicide, temperature, left_index=True, right_index=True)
    common_rows = len(common)
    
    spearman_correlation = common['suicide_fraction'].corr(common['Average yearly temperature (1961–1990, degrees Celsius)'], method="spearman")
    

    return (suicide_rows, temperature_rows, common_rows, spearman_correlation)

def main():
    (suicide_rows, temperature_rows, common_rows, spearman_correlation) = suicide_weather()
    print(f"""
        Suicide DataFrame has {suicide_rows} rows
        Temperature DataFrame has {temperature_rows} rows
        Common DataFrame has {common_rows} rows
        Spearman correlation: {spearman_correlation:.1}""")

if __name__ == "__main__":
    main()
