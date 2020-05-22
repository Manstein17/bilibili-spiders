import mysql.connector
import pandas as pd


conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()

def get_vip_datas():
    sql = 'SELECT vipType as 用户,COUNT(*) as 个数 FROM users GROUP BY vipType'
    a = pd.read_sql(sql,conn)
    b = a.head(199988)
    print('用户付费数据')
    print(b)

def get_sex_datas():
    sql = 'SELECT sex as 性别,COUNT(*) as 个数 FROM users GROUP BY sex'
    a = pd.read_sql(sql, conn)
    b = a.head(199988)
    print('用户性别数据')
    print(b)

def get_upload_datas():
    sql = 'select count(*),upload from users group by upload having upload = 0'
    sql2 = 'select count(*),upload from users group by upload having upload > 100'
    a1 = pd.read_sql(sql, conn)
    b1 = a1.head(199988)
    a2 = pd.read_sql(sql2, conn)
    b2 = a2.head(199988)
    print('投稿用户数量')
    print(b1)
    print('投稿超过100次的ip主')
    print(b2)



get_sex_datas()
print('\n')
get_vip_datas()
print('\n')
get_upload_datas()








