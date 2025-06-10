import pandas as pd
import numpy as np

#Showing all columns
pd.set_option('display.max_columns', None)


df = pd.read_csv('./extrovert-introvert-analysis/data/personality_dataset.csv')



print(df.head())


#Check Column Names
print(df.columns.tolist())

#Structure
print(df.info())

#Summarize Numeric Data

print(df.describe(include='object'))

#Null and duplicated
print(df.isnull().sum())
print(df.duplicated().sum())