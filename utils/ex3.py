'''
Description: 
Autor: Au3C2
Date: 2021-11-23 21:07:08
LastEditors: Au3C2
LastEditTime: 2021-11-23 21:24:19
'''
import pandas as pd

def clean(df):
    n = len(df)
    drop_list = []
    nan_count, nan_ratio = [], []
    for f in df.columns:
        num_nan = df[f].isnull().sum()
        nan_count.append(num_nan)
        nan_ratio.append(num_nan/n)
        if num_nan/n >0.6:
            drop_list.append(f)
    df = df.drop(drop_list,axis=1)
    return df, nan_count, nan_ratio

df = pd.read_csv('utils/test.csv')
df, nan_count, nan_ratio = clean(df)
print(df)



        
