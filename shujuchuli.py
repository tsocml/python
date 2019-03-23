import numpy as np
import pandas as pd
from pandas import Series,DataFrame
df = pd.read_csv(r'C:\Users\Administrator\Desktop\education_data\5_chengji.csv')
df = df.drop(['mes_TestID','mes_dengdi','mes_T_Score','mes_Z_Score','exam_numname','mes_Score','exam_sdate','exam_type','mes_sub_name'],axis=1)
a = df.exam_number.values
a = a.tolist()
def find_repeat(source,elmt):
    elmt_index=[]
    s_index = 0;e_index = len(source)
    while(s_index < e_index):
        try:
            temp = source.index(elmt,s_index,e_index)
            elmt_index.append(temp)
            s_index = temp + 1
        except ValueError:
            break
        return elmt_index
print()


