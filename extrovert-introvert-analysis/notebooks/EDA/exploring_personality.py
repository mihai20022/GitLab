import pandas as pd

df = pd.read_csv("extrovert-introvert-analysis/data/dataset_cleaned.csv", index_col=False)
print(df)
def numeric_columns(dataframe):
    df = dataframe.select_dtypes(include='number')
    return df.columns

numeric_columns = numeric_columns(df)

print(df.groupby('Personality').mean())



