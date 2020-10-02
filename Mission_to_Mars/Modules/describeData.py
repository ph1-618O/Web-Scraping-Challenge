# Comment: Write file creates a module that can be imported with dependencies, %%writefile -a describeData.py appends, remove if func is changed
# Comment: This function prints stats for strings and integer value columns
import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime

def describeData(dataFrameName):
    print('Executing describeData...')
    print('-------------------------------')
    global keyHeaders, colsData, stringDescribe, intDescribe, keyStr, KeyInt
    keyStr, keyInt, keyHeaders, intDescribe, stringDescribe = [], [], [], [], []
    for key, value in dataFrameName.items():
        #grabs cols as keys into list
        keyHeaders.append(key)
    for i in keyHeaders:
        #checks the cols data if string
        if isinstance(dataFrameName[i][0], (str)):
            stringDescribe.append(dataFrameName[keyHeaders][i].describe())
        else:
            intDescribe.append(dataFrameName[keyHeaders][i].describe())
    stringDescribe = pd.DataFrame.from_dict(dict(zip(keyHeaders, stringDescribe)), orient='index')
    intDescribe = pd.DataFrame.from_dict(dict(zip(keyHeaders, intDescribe)), orient='index') 
    #adding pretty print to dataframes, don't forget import statment when copying code
    print('-------------------------------')
    print('Object Describe Dataframe')
    print('-------------------------------')
    display(HTML(stringDescribe.to_html()))
    #print(stringDescribe)
    print('-------------------------------')
    print('Integer/FloatDescribe Dataframe')
    print('-------------------------------')
    display(HTML(intDescribe.to_html()))
    #print(intDescribe)
    lengthofDF = len(dataFrameName)
    print('-------------------------------')
    print(f'Dataframe Length: {lengthofDF}')
    print('-------------------------------')
    columnNames = dataFrameName.columns.tolist()
    print(f'ColumnNames: \n{columnNames}')
# Comment: by ph1-6180
