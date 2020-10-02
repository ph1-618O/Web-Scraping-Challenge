# Comment: Write file creates a module that can be imported with dependencies, %%writefile -a getTypes.py, remove if func is changed

import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime

#getTypes analyzes a DataFrame's column types
def main():
    def getTypes(dataFrameName): #0
        print('Executing getTypes...')
        print('------------------')
        dtypesSeries = dataFrameName.dtypes #1
        dtypesDF = dtypesSeries.to_frame().reset_index() #2
        dtypesDF = dtypesDF.rename(columns={"index": "ColumnName", 0: "DataType"}) #3
        columnNames = dtypesDF.columns.tolist() #4
        #print(columnNames) #5
        newColumns = dtypesDF['DataType'].unique().tolist() #6
        dtypesList = [] #7
        for i in newColumns:
            dtypesList.append(str(i))
        print('Unique values in dtypesDF::') #8
        print('---------------------------')
        for i in dtypesList: 
            print(i)
        print('---------------------------')
        print(f'Lenght of dtypesDF:: {len(dtypesDF)}') #9
        print('---------------------------')
        dtypesDict = {dtypesDF['ColumnName'][i]: dtypesDF['DataType'][i] for i in range(len(dtypesDF['ColumnName']))}
        dictSlice = dict(list(dtypesDict.items())[0: 5]) #11
        #print(dictSlice)
        counter = 0 #12
        dtypesGlobalsList = dtypesList
        for i in dtypesList: #13
            print(f'Global DataFrame Created:: {i}') #14
            dtypesGlobalsList = dtypesDF.loc[(dtypesDF['DataType'] == i)] #15
            globals()[i] = dtypesGlobalsList #16
            globals()[i] = globals()[i].drop(['DataType'], axis=1).reset_index() #17
            globals()[i] = globals()[i].rename(columns={"ColumnName": i}) #18
            globals()[i] = globals()[i].sort_values(i) #19
            counter += 1
            #display(HTML(globals()[i].to_html())) #20
        dtypesSummaryDF = pd.concat([int64, object, float64], axis=1, sort=False) #21
        columnName = dtypesSummaryDF.columns.tolist() #22
        #print(columnName) #23
        counter = 0
        removeIndex = []
        for i in columnName: #24
            if i != 'index':
                removeIndex.append(columnName.pop(counter))
                counter += 1
        #print(removeIndex)
        dtypesSummaryDF.drop(columns = removeIndex, inplace=True) #25
        print('---------------------------')
        print(f'DataFrame Types::')
        print('---------------------------')
        display(HTML(dtypesSummaryDF.to_html())) #26

    

if __name__ == "__main__":
    main()
    
# <! getTypes( ):
# /0/ getTypes analyzes a DataFrame's column types
# /1/ Get dtypes as series
# /2/ Make dataframe out of dtypes, output is messy next steps to format
# /3/ Rename columns
# /4/ Get column names list
# /5/ Print column names list
# /6/ DataFrame is long and uncompressed attempting to create a smaller one with column names as rows
# /7/ Setting up list to get unique data types
# /8/ Printing out the unique data types for observation
# /9/ Getting length before manipulation
# /10/ Creating a Dictionary to Pair values and flip keys/cols and values/rows
# /11/ Grabbing a slice of the dictionary to confirm format
# /12/ Setting up variables for lists and counter
# /13/ For loop to manipulate dtypesList into Global Variables with individual dataframes
# /14/ Print statement to confirm globals creation
# /15/ Matching the data to the dtypesList/dtypesGlobalList into each new global variable
# /16/ Defining globals into dataframes
# /17/ Dropping the Datatype column, keeping only Column Name from Original DF
# /18/ Renaming the ColumnName column to match the global variable name
# /19/ Sorting the ColumnName names alphabetically
# /20/ Displaying each dataframe as HTML within Jupyter//must have import statment in dependencies
# /21/ Merging/Concatenating global dataframes into one Dataframe
# /22/ Creating list of column names to remove extra indicies
# /23/ Printing list to confirm
# /24/ For loop to pop instances that do not equal 'Index'// This is important because there may be many more dtypes in globals()[i] and there must be duplicates in list to drop all at once
# /25/ Dropping removeIndex list
# /26/ Displaying Final DF with all original DF column names as Html under their datatype
# Comment: by ph1-6180
    
