import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)
df = pd.read_csv('./extrovert-introvert-analysis/data/dataset_cleaned.csv')
print(df)

df['Personality']=df['Personality'].map({'Introvert': 0, 'Extrovert': 1})
#checking which featurea are binary
def binary_check(dataframe):
    for col in dataframe.columns:
        if dataframe[col].nunique() == 2:
            print(col, dataframe[col].unique())

def cross_tab_generation_binary(dataframe, columns):
    for col in columns:
        print(pd.crosstab(dataframe['Personality'],dataframe[col], normalize='index'))


binary_check(df)
columns = ['Drained_after_socializing','Stage_fear']
cross_tab_generation_binary(df,columns)

numeric_df = df.select_dtypes(include='number')
print(numeric_df)

correlation_matrix = numeric_df.corr()
print(correlation_matrix)

mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

plt.figure(figsize=(10,6))

sns.heatmap(correlation_matrix, mask=mask,annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.tight_layout()
plt.savefig("./extrovert-introvert-analysis/reports/correlation_heatmap.png", dpi=300, bbox_inches='tight')

print(df['Stage_fear'].value_counts(normalize=True))
print(df['Drained_after_socializing'].value_counts(normalize=True))

print(df.corr()['Personality'].sort_values())

df = df.drop(axis= 1, columns=['Stage_fear'])

df.to_csv('extrovert-introvert-analysis/data/dataset_ready_modeling.csv')