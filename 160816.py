#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
v = numpy.array([1,2,3,4])
#print(v.shape)

m = numpy.array([[1, 2], [3, 4]])
#print(m[0,0])

# print(m[0,:]) #0번째 row의 모든 값들을 출력해라.
# print(m[:,1]) #column의 1번째 값들을 출력해라.
import pandas as pd

m[:,1] = 0
# print(m)

v1 = numpy.arange(0, 5)
# print(v1)
v1 = pd.DataFrame(v1)
print(v1.mean())
print(v1.var())
print(v1.std())
#pandas - 2차원 배열
#series - 1차원 배열
#series들을 엮어 놓은 것이 2차원이 되고 그것이 dataframe이다.
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 
'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

e = {'kapsu' : pd.Series([10,20,30], index = ['x','y','z'] ),
}
ef = pd.DataFrame(e);
# print(ef['kapsu'])
# print(ef)

df = pd.DataFrame(d)
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] >2
# print(df)
# print(df['one'])
# print(df.loc['b'])