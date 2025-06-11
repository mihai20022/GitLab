import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df = pd.read_csv('./extrovert-introvert-analysis/data/dataset_cleaned.csv')



print(df.describe())

def histograms_columns(dataframe):
    numeric_columns = dataframe.select_dtypes(include='number')
    for col in numeric_columns:
        sns.histplot(dataframe[col],kde=True)
        plt.show()
        sns.boxplot(dataframe[col])
        plt.show()
        print('Skewness for {col}:', dataframe[col].skew())

histograms_columns(df)

    