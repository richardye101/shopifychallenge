import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def get_data(file_name):
    df = pd.read_csv('dataset.csv')
    return df

def AOV(df):
    # total_order_amt = df['order_amount'].sum()
    # total_items = df['total_items'].sum()
    # temp = df[['order_amount','total_items']].sort_values(by=['order_amount'])
    # print(temp)
    # print(df[['order_amount','total_items']])
    avg_order_amt = df['order_amount']/df['total_items']
    avg_total = avg_order_amt.sum() / avg_order_amt.count()
    return avg_total

if __name__ == '__main__':
    filename = 'dataset.csv'
    df = get_data(filename)
    d = AOV(df)
    print(AOV(df))
    # print(df.head())
    # print(df['order_amount'].sum() / df.shape[0])
    # print(df['total_items'].sum())
    print(df['order_amount'].sum() / df['total_items'].sum())
