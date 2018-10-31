# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:55:31 2018
Add record into the database from csv file
@author: Ba La
"""
import csv
from DbCon import DatabaseOperations as db
import time
def read_file(filename,opt_data=0):
    """
        Read the csv into list of lists
        and get columns 1,2,9,11
        If opt_data == 0 do not add the full name
        if opt_data == 1 add the full name
    """
    # List to hold all the rows
    required_record_data = []
    with open(filename,'r',newline="") as file_handle:
        csv_reader = csv.reader(file_handle) # csv reader to read each row
        for row in csv_reader: # iterate through each row
            # check opt_data and prepare the correct data
            if(opt_data == 1):
                #TODO: Add code here
                pass
            else:
                #TODO: Add code here
                pass
            #TODO: Append data to the required_record_data
    return required_record_data

def update_database(filename):
    #TODO: Create the database connection
    data = read_file(filename)
    for data_row in data:
        #TODO: Insert the row into the database
        pass
if __name__ == "__main__":
    start = time.time()
    update_database("us-500.csv")
    end = time.time()
    print(end-start)
    
