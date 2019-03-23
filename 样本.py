from pandas import Series,DataFrame
import pandas as pd
import numpy as np
df = pd.read_csv(r'泉水温度.txt')
df = df.drop(['20050101'],axis=1)
for a in range(len(df)):
    b = a+30
    dh = df.ix[a:b,:]
    L = dh.values
    K = pd.DataFrame(L,columns=['0'])
    if b >= (len(df)-1):
        break
    K.to_csv(r'C:\Users\Administrator\Desktop\新建文件夹 (2)\str(%d).csv'%a)