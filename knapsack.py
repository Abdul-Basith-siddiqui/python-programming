# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:24:24 2020

@author: Nirav
"""
import numpy as np
n = int(input('total different values'))
c = int(input('enter knapsack capacity'))
w=[]
p=[]

k = np.zeros((n+1,c+1),int)

print(k)
print(k[1,3])
for i in range(n):
    print('enter values of weight and profit for item %d'%i)
    w.append(int(input()))
    p.append(int(input()))


for i in range(n):
    for j in range(c):
        if(i==0 and j<w[i]):
            k[i][j]=0
        elif(i==0):
            k[i][j]=p[0]
        elif(j<w[i]):
            k[i][j]=k[i-1][j]
        else:
            k[i][j] = max(k[i-1][j],p[i]+k[i-1][j-w[i]])

print('maximum profit = %d'%k[n-1][c-1])            