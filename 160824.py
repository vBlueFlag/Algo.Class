#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle('data/000040.data')
df = df['Open']
df.plot()
plt.show()

# print (df)
# print (df.mean())
# print (df['Open'].mean())

# for i in range(5):
#     ds.append(df[i]['Open'].mean())

# print(ds)

# for i in range(5):
#     ds.append(df[i]['Open'])

# for v in ds:
#     v.plot()
# plt.show()

# ds[0]['Open'].plot()
# ds[1]['Open'].plot()
# ds[2]['Open'].plot()
# ds[3]['Open'].plot()
# ds[4]['Open'].plot()
# plt.show()