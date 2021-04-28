#!/usr/bin/env python3

import pandas as pd
import numpy as np


## Part 1

data_url = "https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv"

data = pd.read_csv(data_url, na_values='N.A.')
print(f'There are {data.shape[0]} rows including non-numeric values')
data = data.dropna()
data.iloc[:, -1] = data.iloc[:, -1].astype(np.float64)
print(f'There are {data.shape[0]} rows')

## Part 2

data = data.rename(columns={
    'Revenue (in millions)' : 'Revenue',
    'Profit (in millions)' : 'Profit',
})
data.to_json('data2.json', indent=2, orient='records')
data.sort_values(by='Profit', inplace=True, ascending=False)
print(data.head(20).to_string(index=False))

# print(data.info())
# print(data.describe())
