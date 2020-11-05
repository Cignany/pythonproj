# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
Pandas Basics: Reading Files, Summarizing, Handling Missing Values, Filtering, Sorting
'''

# read in the CSV file from a URL
drinks = pd.read_csv('drinks.csv')
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/python-data-analysis-workshop/master/drinks.csv')
type(drinks)

# examine the data
drinks                  # print the first 30 and last 30 rows
drinks.head()           # print the first 5 rows
drinks.tail()           # print the last 5 rows
drinks.describe()       # describe any numeric columns
drinks.info()           # concise summary

# find missing values in a DataFrame
drinks.isnull()         # DataFrame of booleans
drinks.isnull().sum()   # convert booleans to integers and add

# handling missing values
drinks.dropna()             # drop a row if ANY values are missing
drinks.fillna(value='NA')   # fill in missing values

# fix the original import
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/python-data-analysis-workshop/master/drinks.csv', na_filter=False)
drinks.isnull().sum()

# selecting a column ('Series')
drinks['continent']
drinks.continent            # equivalent
type(drinks.continent)

# summarizing a non-numeric column
drinks.continent.describe()
drinks.continent.value_counts()

# selecting multiple columns
drinks[['country', 'beer_servings']]
my_cols = ['country', 'beer_servings']
drinks[my_cols]

# add a new column as a function of existing columns
drinks['total_servings'] = drinks.beer_servings + drinks.spirit_servings + drinks.wine_servings
drinks.head()
