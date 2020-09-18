# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:53:05 2020

@author: Daniyal Kabir
"""

import pandas


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''
   
    return pandas.read_csv(filename)


def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input
    and returns the median of the column name
    Returns: float'''
   
    return data_frame[column_name].median()
   
   
def find_highest_mpg(data_frame, country):
    '''This function receives a DataFrame and country as input and returns
    the model of the country cars (str) with the highest mpg and the highest mpg.
    Returns: str, float'''
   
    df = data_frame.loc[data_frame['origin'] == country, ['name', 'mpg']]
    max_val = df['mpg'].max()
    df.set_index('mpg', inplace=True)
    name = df['name'][max_val]
   
    return name, max_val


def main():
    filename = "mpg.csv"
    data_frame = read_csv_2(filename)

    print("First 5 rows of columns mpg and horsepower:")
    print(data_frame.loc[:4, ['mpg', 'horsepower']])
    print()

    print("Last 5 rows of columns mpg, horsepower, model_year, and name:")
    print(data_frame[['mpg', 'horsepower', 'model_year', 'name']].tail())
    print()
   
    acc_median = find_median_2(data_frame, 'acceleration')
    print("Mean 0-60 mph acceleration time (in sec): {:.1f}\n".format(acc_median))
   
    car_name, country_max = find_highest_mpg(data_frame, 'usa')
    print("Highest MPG US car:")
    print(car_name, "-", country_max, "mpg")
       
   
if __name__ == '__main__':
    main()