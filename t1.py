#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy
import matplotlib.pyplot as plt

a = {'frq': pd.Series([1,2,4,2,1]), 'score': pd.Series([7,9,10,11,13])}
b = {'frq': pd.Series([1,1,2,2,2,1,1]), 'score': pd.Series([7,8,9,10,11,12,13])}
c = {'frq': pd.Series([2,1,2,3,1,1,1]), 'score': pd.Series([3,6,7,10,11,13,30])}


player1 = pd.DataFrame(a)
player2 = pd.DataFrame(b)
player3 = pd.DataFrame(c)
avg1 = sum(player1['frq'] * player1['score']) / player1['frq'].sum()
avg2 = sum(player2['frq'] * player2['score']) / player2['frq'].sum()
avg3 = sum(player3['frq'] * player3['score']) / player3['frq'].sum()

# print(len(player1['frq']))
p1 = []
for i in range(len(player3['frq'])):
    for j in range(player3['frq'][i]):
        p1.append( player3['score'][i])

p1 = numpy.array(p1) # numpy를 쓸 때는 이렇게 array()안에 배열 넣어주면 되네.

print(p1.mean())
print(p1.std())

# print(avg)
# print(board())
# print(board.median())
# print(board.clip_lower())
# plt.hist(board['frq'])
# plt.plot(board)
# plt.show()

# pandas 라이브러리 이용

# print(arr)
# x = pd.Series(range(1,7))
# print(x)
# print(x.mean())
# print(x.var())#pandas는 어떻게 var()과 std()를 구하는 걸까.
# print(x.std())

# v1 = numpy.arange(1,7)
# print(sum(v1**2)/len(v1)-v1.mean()**2)
# print(v1.mean())
# print(v1.var())
# print(v1.std())