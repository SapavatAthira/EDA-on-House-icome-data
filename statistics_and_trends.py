"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots()
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col].dropna())
    excess_kurtosis =  ss.kurtosis(df[col].dropna(), fisher=True)
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    print("Dataset Overview:\n", df.describe())
    print("First few rows:\n", df.head())
    
    numeric_df = df.select_dtypes(include=[np.number])
    print("Correlation Matrix:\n", numeric_df.corr())
    
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
   skewness_desc = "not skewed" if -2 < moments[2] < 2 else ("right-skewed" if moments[2] > 2 else "left-skewed")
    kurtosis_desc = "mesokurtic" if -2 < moments[3] < 2 else ("leptokurtic" if moments[3] > 2 else "platykurtic")
    print(f'The data was {skewness_desc} and {kurtosis_desc}.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'Mthly_HH_Income'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
