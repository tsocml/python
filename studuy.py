import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import pandas as pd

ojbk = {'name':['周','刘','宋','侯'],
'year':[20, 18, 19, 19],
'tall':[170, 173, 172, 172]}
ok = DataFrame(ojbk)
ok1 = DataFrame(ojbk,columns=['name', 'year', 'tall', 'weight'],index=['a', 'b', 'c', 'd'])
ok1['weight'] = Series([140,180,170,120],index=['a', 'c', 'b', 'd'])
ok1 = ok1.drop(['name'],axis=1)
s = ok1['weight']
ok1.sub(s)
print(ok1.sub(s,axis = 0))