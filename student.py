import numpy as py
import pandas as pd
from pandas import Series,DataFrame
import msvcrt,sys
import csv
a = 123456
p = 123456
l = 3
Q = []
for i in range(0,3):
    zh = int(input('请输入登陆账号:'))
    if zh == a:
        pwd = int(input('请输入登陆密码:'))
        if pwd == p:
            print('登陆成功，欢迎你，刘老师。',end='')
            break
        else:
            l -= 1
            print('密码错误，请重新输入,你还剩下%d次机会'%l)
    else:
        l -= 1
        print('账号错误，请重新输入，你还剩下%d次机会'%l)
if zh == a and pwd == p:
    print('请继续操作：')
else:
    print('滚啊,sb')
    sys.exit()
inf = {"zhanghao":zh,"password":pwd}
Q.append(inf)
Q = pd.DataFrame(Q)
Q.to_csv(r'C:\Users\Administrator\Desktop\a.csv')
#菜单
def menu():
    menu_info = '''＋－－－－－－－－－－－－－－－－－－－－－－＋
    ｜ 1）载入第一个学生信息                     |
     | 2 )添加学生信息                           ｜
    ｜ 3 )显示所有学生的信息                     ｜
    ｜ 4）删除学生信息                           ｜
    ｜ 5）修改学生信息                           ｜
    ｜ 退出：其他任意按键＜回车＞                ｜
    ＋－－－－－－－－－－－－－－－－－－－－－－＋
    '''
    print(menu_info)
#载入第一个学生信息

def student_info():
    L = []
    while True:
        n = input('请输入学生姓名:')
        if not n:
            break
        try:
            age = int(input('请输入年龄：'))
            grade = int(input('请输入成绩：'))
        except:
            print("输入的啥玩意儿？给老子重新录入")
            continue
        info = {"name":n,"age":age,"grade":grade}
        L.append(info)
        c = pd.DataFrame(L)
        c.to_csv(r'C:\Users\Administrator\Desktop\b.csv')
        return L
def add_student_info():
    S = []
    while True:
        n = input('请输入学生姓名:')
        if not n:
            break
        try:
            age = int(input('请输入年龄：'))
            grade = int(input('请输入成绩：'))
        except:
            print("输入的啥玩意儿？给老子重新录入")
            continue
        info1 = {"name":n,"age":age,"grade":grade}
        S.append(info1)
        s = pd.DataFrame(S)
        s.to_csv(r'C:\Users\Administrator\Desktop\b.csv',mode='a',header=False)
        return S
#查询成绩
def show_student_info():
    df = pd.read_csv(r'C:\Users\Administrator\Desktop\b.csv')
    print(df)
#删除信息
def del_student_info():
    df = pd.read_csv(r'C:\Users\Administrator\Desktop\b.csv')
    print(df)
    e = int(input('请选择想要删除的学生序号：'))
    df = df.drop([e],axis = 0,inplace = False)
    df.to_csv(r'C:\Users\Administrator\Desktop\b.csv')
    return 0
#修改信息
def mod_student_info():
    df = pd.read_csv(r'C:\Users\Administrator\Desktop\b.csv')
    print(df)
    e1 = int(input('请选择想要修改的学生序号：'))
    e2 = input('请选择想要修改的学生数据类型：')
    e3 = input('修改的数值:')
    df.loc[e1,e2] = e3
    df.to_csv(r'C:\Users\Administrator\Desktop\b.csv')
    return 0
def main():
    while True:
        # print(student_info)
        menu()
        number = input("请输入选项：")
        if number == '1':
            student_info()
        elif number == '2':
            add_student_info()
        elif number == '3':
            show_student_info()
        elif number == '4':
            del_student_info()
        elif number == '5':
            mod_student_info()
main()








