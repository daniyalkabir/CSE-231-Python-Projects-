# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:52:24 2020

@author: Daniyal Kabir
"""

import pandas #import pandas module
import time  #used to calculate execution time
import csv  #import csv module


def read_csv_1(filename):
    ''' This function read a csv file into a list of lists (each line is an element)
    Returns: list of lists'''
   
    fp = open(filename)
   
    reader = csv.reader(fp)
    next(reader)
   
    return [line for line in reader]


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame.
    Returns: DataFrame'''
   
    return pandas.read_csv(filename)

   
def find_median_1(data, index):
    '''
    This function receives a list of lists (data) and an integer index as input
    and calculates and prints the median of the column index.
    '''
           
    index_list = [float(line[index]) for line in data]
   
    index_list.sort()
   
    length = len(index_list)
    if length % 2 == 1: #length is odd
        median = index_list[(length-1)//2]
    else:
        median = (index_list[length//2-1] + index_list[length//2])/2
       
    return round(median, 2)


def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input
    and calculates and prints the median of the column name'''
   
    return round( data_frame[column_name].median() , 2 )
   
   
def main():
    filename = "college_scorecard.csv"
   
    start_time = time.time()
    data_list = read_csv_1(filename)
    time1 = time.time()
    print("read_csv_1: {:.4f}".format((time1 - start_time)*1000))
   
    start_time = time.time()
    data_frame = read_csv_2(filename)
    time2 = time.time()
    print("read_csv_2: {:.4f}".format((time2 - start_time)*1000))
   
    index = 1
    column = data_frame.columns[index]
   
    start_time = time.time()
    median_1 = find_median_1(data_list, index)
    time3 = time.time()
    print("find_median_1 time: {:.4f}".format((time3 - start_time)*1000))
    print("Median: ", median_1)
   
    start_time = time.time()
    median_2 = find_median_2(data_frame, column)
    time4 = time.time()
    print("find_median_2: {:.4f}".format((time4 - start_time)*1000))
    print("Median: ", median_2)
   
   
if __name__ == '__main__':
    main()

