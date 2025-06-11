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


#Assessing the % of missing values

missing_percentage = df.isnull().mean() * 100
print(missing_percentage)

#The distributions of the features are mostly skewed to the right. Median will be applied to the columns

def impute_numeric_median(dataframe):
    numeric_columns= dataframe.select_dtypes(include='number').columns
    print(numeric_columns)

    for col in numeric_columns:
        if dataframe[col].isnull().sum() > 0:
            median_value = dataframe[col].median()
            dataframe[col] = dataframe[col].fillna(median_value)

def binary_imputation_categorical(dataframe):
    binary_columns= []

    for col in dataframe.columns:
        unique_values = dataframe[col].dropna().unique()
        if len(unique_values) == 2:
            binary_columns.append(col)
    
    for col in binary_columns:
        if dataframe[col].isnull().sum() > 0:
            mod_value = dataframe[col].mode()[0]
            dataframe[col] = dataframe[col].fillna(mod_value)

def select_binary_columns(dataframe, exclude_columns=None):
    binary_columns=[]

    for col in dataframe.columns:
        if len(dataframe[col].dropna().unique()) == 2:
            if col not in exclude_columns:
                print(col)
                binary_columns.append(col)
    return binary_columns

def encode_binary_columns(dataframe):
    binary_map={'Yes':1, 'No':0}
    binary_columns = select_binary_columns(dataframe, exclude_columns=['Personality'])
    print(binary_columns)
    for col in binary_columns:
        dataframe[col]=dataframe[col].map(binary_map)
    


impute_numeric_median(df)
binary_imputation_categorical(df)
encode_binary_columns(df)

print(df)

df.to_csv('./extrovert-introvert-analysis/data/dataset_cleaned.csv',index=False)