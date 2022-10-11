# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:39:38 2022

@author: Muqeet
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('worker.csv')

data

data.shape

data.info()

data.describe(include='all')

#conversations

data['quarter'].unique()

#converet data to numeric

data['quarter']=[int(-1) for x in data['quarter']]

data['quarter']

#convert date to datetime object
data["date"]=pd.to_datetime(data["date"])

data["date"].unique()

#convert department and day of week into numbers

data['department']=[a.strip() for a in data['department']]
data['department']

#converting departmental data into numerical data
data['department']=[0 if x=='sweing' else 1 for x in data['department']]
data['department']


day_to_num={
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6
    }

data["day"]=[day_to_num[x] for x in data["day"]]
data["day"]

#as wip has more null values
data["wip"].isnull().sum()



#imputation


from sklearn.impute import SimpleImputer
zero_imputer=SimpleImputer(strategy='constant',fill_value=0)

data['wip']=pd.Series(zero_imputer.fit_transform(np.array(data['wip']).reshape(1,-1)).reshape(-1))

#category

data[['quarter','department','day','team']]=data[['quarter','department','day','team']].apply(lambda x: x.astype('category'))

data.info()


data.describe(include='all',datetime_is_numeric=True)


#data exploration and visualisation














