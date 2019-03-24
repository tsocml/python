import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties
import matplotlib as mpl
df = pd.read_csv(r'C:\Users\Administrator\Desktop\education_data\5_chengji.csv')
df = df.drop(['mes_T_Score','mes_dengdi','mes_TestID','exam_numname','mes_Z_Score','mes_Score','mes_sub_id','exam_sdate'],axis=1)
df = df.set_index('exam_number')
#lb = df.ix[282]#宁波
#zp = df.ix[280]#总评
#yq = df.ix[284]#2017期中
# yl = df.ix[279]#2016期末
# sx = df.ix[275]#宁波十校
gs = df.ix[235]#2014高三
# yw = df.ix[252]#2015期中
# yl_two = df.ix[277]#2016第二学期
# ys = df.ix[239]#2014期中
#yw_gk = df.ix[241]#宁波2015高考
# lb.to_csv(r'C:\Users\Administrator\Desktop\lb.csv')
# zp.to_csv(r'C:\Users\Administrator\Desktop\zp.csv')
# yq.to_csv(r'C:\Users\Administrator\Desktop\yq.csv')
# yl.to_csv(r'C:\Users\Administrator\Desktop\yl.csv')
# sx.to_csv(r'C:\Users\Administrator\Desktop\sx.csv')
# gs.to_csv(r'C:\Users\Administrator\Desktop\gs.csv')
# yw.to_csv(r'C:\Users\Administrator\Desktop\yw.csv')
# yl_two.to_csv(r'C:\Users\Administrator\Desktop\yl_two.csv')
# ys.to_csv(r'C:\Users\Administrator\Desktop\ys.csv')
# yw_gk.to_csv(r'C:\Users\Administrator\Desktop\yw_gk.csv')
#print(lb)
#删除语文数学英语
gs = gs.astype(str)
x = gs[gs['mes_sub_name'].str.contains('语文')]
y = gs[gs['mes_sub_name'].str.contains('数学')]
z = gs[gs['mes_sub_name'].str.contains('英语')]
gs_l = list(gs.mes_sub_name)
x1 = list(x.mes_sub_name)
y1 = list(y.mes_sub_name)
z1 = list(z.mes_sub_name)
ret = list(set(gs_l) ^ set(x1))
ret1 = list(set(ret) ^ set(y1))
ret2 = list(set(ret1) ^ set(z1))
gs = gs[gs.mes_sub_name.isin(ret2)]
gs1 = gs.set_index('mes_StudentID')
gs2 = gs.mes_StudentID.values
#print(len(gs2))
# for i in gs2:
#     print(gs1.ix[i])
sum = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['物理', '生物', '化学']:
        sum = sum + 1
    elif gs3 == ['物理', '化学', '生物']:
        sum = sum + 1
    elif gs3 == ['生物', '化学', '物理']:
        sum = sum + 1
    elif gs3 == ['生物', '物理', '化学']:
        sum = sum + 1
    elif gs3 == ['化学', '生物', '物理']:
        sum = sum + 1
    elif gs3 == ['化学', '物理', '生物']:
        sum = sum + 1
    else:
        pass
s = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '地理', '历史']:
        s = s + 1
    elif gs3 == ['政治', '历史', '地理']:
        s = s + 1
    elif gs3 == ['历史', '政治', '地理']:
        s = s + 1
    elif gs3 == ['历史', '地理', '政治']:
        s = s + 1
    elif gs3 == ['地理', '政治', '历史']:
        s = s + 1
    elif gs3 == ['地理', '历史', '政治']:
        s = s + 1
    else:
        pass
s1 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '物理', '化学']:
        s1 = s1 + 1
    elif gs3 == ['政治', '化学', '物理']:
       s1 = s1 + 1
    elif gs3 == ['化学', '政治', '物理']:
        s1 = s1 + 1
    elif gs3 == ['化学', '物理', '政治']:
        s1 = s1 + 1
    elif gs3 == ['物理', '政治', '化学']:
        s1 = s1 + 1
    elif gs3 == ['物理', '化学', '政治']:
        s1 = s1 + 1
    else:
        pass
s2 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['历史', '物理', '化学']:
        s2 = s2 + 1
    elif gs3 == ['历史', '化学', '物理']:
       s2 = s2 + 1
    elif gs3 == ['化学', '历史', '物理']:
        s2 = s2 + 1
    elif gs3 == ['化学', '物理', '历史']:
        s2 = s2 + 1
    elif gs3 == ['物理', '历史', '化学']:
        s2 = s2 + 1
    elif gs3 == ['物理', '化学', '历史']:
        s2 = s2 + 1
    else:
        pass
s3 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '物理', '化学']:
        s3 = s3 + 1
    elif gs3 == ['地理', '化学', '物理']:
       s3 = s3 + 1
    elif gs3 == ['化学', '地理', '物理']:
        s3 = s3 + 1
    elif gs3 == ['化学', '物理', '地理']:
        s3 = s3 + 1
    elif gs3 == ['物理', '地理', '化学']:
        s3 = s3 + 1
    elif gs3 == ['物理', '化学', '地理']:
        s3 = s3 + 1
    else:
        pass
s4 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '物理', '生物']:
        s4 = s4 + 1
    elif gs3 == ['政治', '生物', '物理']:
       s4 = s4 + 1
    elif gs3 == ['生物', '政治', '物理']:
        s4 = s4 + 1
    elif gs3 == ['生物', '物理', '政治']:
        s4 = s4 + 1
    elif gs3 == ['物理', '政治', '生物']:
        s4 = s4 + 1
    elif gs3 == ['物理', '生物', '政治']:
        s4 = s4 + 1
    else:
        pass
s5 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '生物', '化学']:
        s5 = s5 + 1
    elif gs3 == ['政治', '化学', '生物']:
       s5 = s5 + 1
    elif gs3 == ['化学', '政治', '生物']:
        s5 = s5 + 1
    elif gs3 == ['化学', '生物', '政治']:
        s5 = s5 + 1
    elif gs3 == ['生物', '政治', '化学']:
        s5 = s5 + 1
    elif gs3 == ['生物', '化学', '政治']:
        s5 = s5 + 1
    else:
        pass
s6 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '生物', '化学']:
        s6 = s6 + 1
    elif gs3 == ['地理', '化学', '生物']:
       s6 = s6 + 1
    elif gs3 == ['化学', '地理', '生物']:
        s6 = s6 + 1
    elif gs3 == ['化学', '生物', '地理']:
        s6 = s6 + 1
    elif gs3 == ['生物', '地理', '化学']:
        s6 = s6 + 1
    elif gs3 == ['生物', '化学', '地理']:
        s6 = s6 + 1
    else:
        pass
s7 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['历史', '生物', '化学']:
        s7 = s7 + 1
    elif gs3 == ['历史', '化学', '生物']:
       s7 = s7 + 1
    elif gs3 == ['化学', '历史', '生物']:
        s7 = s7 + 1
    elif gs3 == ['化学', '生物', '历史']:
        s7 = s7 + 1
    elif gs3 == ['生物', '历史', '化学']:
        s7 = s7 + 1
    elif gs3 == ['生物', '化学', '历史']:
        s7 = s7 + 1
    else:
        pass
s8 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '物理', '生物']:
        s8 = s8 + 1
    elif gs3 == ['地理', '生物', '物理']:
       s8 = s8 + 1
    elif gs3 == ['生物', '地理', '物理']:
        s8 = s8 + 1
    elif gs3 == ['生物', '物理', '地理']:
        s8 = s8 + 1
    elif gs3 == ['物理', '地理', '生物']:
        s8 = s8 + 1
    elif gs3 == ['物理', '生物', '地理']:
        s8 = s8 + 1
    else:
        pass
s9 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['历史', '物理', '生物']:
        s9 = s9 + 1
    elif gs3 == ['历史', '生物', '物理']:
       s9 = s9 + 1
    elif gs3 == ['生物', '历史', '物理']:
        s9 = s9 + 1
    elif gs3 == ['生物', '物理', '历史']:
        s9 = s9 + 1
    elif gs3 == ['物理', '历史', '生物']:
        s9 = s9 + 1
    elif gs3 == ['物理', '生物', '历史']:
        s9 = s9 + 1
    else:
        pass
s10 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '地理', '物理']:
        s10 = s10 + 1
    elif gs3 == ['政治', '物理', '地理']:
        s10 = s10 + 1
    elif gs3 == ['物理', '政治', '地理']:
        s10 = s10 + 1
    elif gs3 == ['物理', '地理', '政治']:
        s10 = s10 + 1
    elif gs3 == ['地理', '政治', '物理']:
        s10 = s10 + 1
    elif gs3 == ['地理', '物理', '政治']:
        s10= s10 + 1
    else:
        pass
s11 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '地理', '化学']:
        s11 = s11 + 1
    elif gs3 == ['政治', '化学', '地理']:
        s11 = s11 + 1
    elif gs3 == ['化学', '政治', '地理']:
        s11 = s11 + 1
    elif gs3 == ['化学', '地理', '政治']:
        s11 = s11 + 1
    elif gs3 == ['地理', '政治', '化学']:
        s11 = s11 + 1
    elif gs3 == ['地理', '化学', '政治']:
        s11 = s11 + 1
    else:
        pass
s12 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '地理', '生物']:
        s10 = s10 + 1
    elif gs3 == ['政治', '生物', '地理']:
        s10 = s10 + 1
    elif gs3 == ['生物', '政治', '地理']:
        s10 = s10 + 1
    elif gs3 == ['生物', '地理', '政治']:
        s10 = s10 + 1
    elif gs3 == ['地理', '政治', '生物']:
        s10 = s10 + 1
    elif gs3 == ['地理', '生物', '政治']:
        s10= s10 + 1
    else:
        pass
s13 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '物理', '历史']:
        s13 = s13 + 1
    elif gs3 == ['政治', '历史', '物理']:
       s13 = s13 + 1
    elif gs3 == ['历史', '政治', '物理']:
        s13 = s13 + 1
    elif gs3 == ['历史', '物理', '政治']:
        s13 = s13 + 1
    elif gs3 == ['物理', '政治', '历史']:
        s13 = s13 + 1
    elif gs3 == ['物理', '历史', '政治']:
        s13 = s13 + 1
    else:
        pass
s14 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '化学', '历史']:
        s14 = s14 + 1
    elif gs3 == ['政治', '历史', '化学']:
       s14 = s14 + 1
    elif gs3 == ['历史', '政治', '化学']:
        s14 = s14 + 1
    elif gs3 == ['历史', '化学', '政治']:
        s14 = s14 + 1
    elif gs3 == ['化学', '政治', '历史']:
        s14 = s14 + 1
    elif gs3 == ['化学', '历史', '政治']:
        s14 = s14 + 1
    else:
        pass
s15 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['政治', '生物', '历史']:
        s13 = s13 + 1
    elif gs3 == ['政治', '历史', '生物']:
       s13 = s13 + 1
    elif gs3 == ['历史', '政治', '生物']:
        s13 = s13 + 1
    elif gs3 == ['历史', '生物', '政治']:
        s13 = s13 + 1
    elif gs3 == ['生物', '政治', '历史']:
        s13 = s13 + 1
    elif gs3 == ['生物', '历史', '政治']:
        s13 = s13 + 1
    else:
        pass
s16 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '物理', '历史']:
        s16 = s16 + 1
    elif gs3 == ['地理', '历史', '物理']:
       s16 = s16 + 1
    elif gs3 == ['历史', '地理', '物理']:
        s16 = s16 + 1
    elif gs3 == ['历史', '物理', '地理']:
        s16 = s16 + 1
    elif gs3 == ['物理', '地理', '历史']:
        s16 = s16 + 1
    elif gs3 == ['物理', '历史', '政治']:
        s16 = s16 + 1
    else:
        pass
s17 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '生物', '历史']:
        s13 = s13 + 1
    elif gs3 == ['地理', '历史', '生物']:
       s13 = s13 + 1
    elif gs3 == ['历史', '地理', '生物']:
        s13 = s13 + 1
    elif gs3 == ['历史', '生物', '地理']:
        s13 = s13 + 1
    elif gs3 == ['生物', '地理', '历史']:
        s13 = s13 + 1
    elif gs3 == ['生物', '历史', '地理']:
        s13 = s13 + 1
    else:
        pass
s18 = 0
for i in gs2:
    gs3 = list(gs1.ix[i].mes_sub_name.values)
    if gs3 == ['地理', '化学', '历史']:
        s14 = s14 + 1
    elif gs3 == ['地理', '历史', '化学']:
       s14 = s14 + 1
    elif gs3 == ['历史', '地理', '化学']:
        s14 = s14 + 1
    elif gs3 == ['历史', '化学', '地理']:
        s14 = s14 + 1
    elif gs3 == ['化学', '地理', '历史']:
        s14 = s14 + 1
    elif gs3 == ['化学', '历史', '地理']:
        s14 = s14 + 1
    else:
        pass
L = [sum,s,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18]
#可视化
def getChineseFont():
    return FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf')
label = ['理综','文综']
color = 'red','blue'
plt.pie(L,colors=color,labels = label,autopct='%1.1f%%')
plt.title(u'关于六选三的占比', fontproperties=getChineseFont(), fontsize=12)
plt.legend(prop=getChineseFont(), loc=0, bbox_to_anchor=(0.82, 1))
plt.show()
