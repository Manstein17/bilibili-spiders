import mysql.connector
import pandas as pd


conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()


def get_vip_datas():
    sql = 'select vipType as 用户,count(*) as 个数 from users group by vipType'
    a = pd.read_sql(sql, conn)
    b = a.head(100)
    print('用户付费数据')
    print(b)


def get_sex_datas():
    sql = 'select sex as 性别,count(*) as 个数 from users group by sex'
    a = pd.read_sql(sql, conn)
    b = a.head(10)
    print('用户性别数据')
    print(b)


def get_upload_datas():
    sql = 'select count(*) as 纯观众个数 from users where upload = 0'
    sql2 = 'select * from users order by upload desc limit 10;'
    a1 = pd.read_sql(sql, conn)
    b1 = a1.head(10)
    a2 = pd.read_sql(sql2, conn)
    b2 = a2.head(10)
    print('纯观众用户数量')
    print(b1)
    print('投稿数排名前10')
    print(b2)


def get_level_datas():
    sql = 'select level as 等级,count(*) as 个数 from users group by level'
    a = pd.read_sql(sql, conn)
    b = a.head(10)
    print('用户等级数据')
    print(b)


def get_fan_datas():
    sql1 = 'select count(*) as 粉丝数为0 from users where fans = 0'
    sql2 = 'select count(*) as 粉丝数为个级 from users where fans between 1 and 9'
    sql3 = 'select count(*) as 粉丝数为十级 from users where fans between 10 and 99'
    sql4 = 'select count(*) as 粉丝数为百级 from users where fans between 100 and 999'
    sql5 = 'select count(*) as 粉丝数为千级 from users where fans between 1000 and 9999'
    sql6 = 'select count(*) as 粉丝数为万级 from users where fans between 10000 and 99999'
    sql7 = 'select count(*) as 粉丝数为十万级 from users where fans between 100000 and 999999'
    sql8 = 'select count(*) as 粉丝数为百万级 from users where fans between 1000000 and 9999999'
    sql9 = 'select count(*) as 粉丝数为千万级 from users where fans between 10000000 and 99999999'
    print('用户粉丝量级数据')
    a1 = pd.read_sql(sql1, conn)
    b1 = a1.head(10)
    print(b1)
    a2 = pd.read_sql(sql2, conn)
    b2 = a2.head(10)
    print(b2)
    a3 = pd.read_sql(sql3, conn)
    b3 = a3.head(10)
    print(b3)
    a4 = pd.read_sql(sql4, conn)
    b4 = a4.head(10)
    print(b4)
    a5 = pd.read_sql(sql5, conn)
    b5 = a5.head(10)
    print(b5)
    a6 = pd.read_sql(sql6, conn)
    b6 = a6.head(10)
    print(b6)
    a7 = pd.read_sql(sql7, conn)
    b7 = a7.head(10)
    print(b7)
    a8 = pd.read_sql(sql8, conn)
    b8 = a8.head(10)
    print(b8)
    a9 = pd.read_sql(sql9, conn)
    b9 = a9.head(10)
    print(b9)


def get_fan_sorting_datas():
    sql = 'select * from users order by fans desc limit 10'
    print('用户粉丝量排名前10数据')
    a = pd.read_sql(sql, conn)
    b = a.head(20)
    print(b)

get_sex_datas()
print('\n')
get_vip_datas()
print('\n')
get_upload_datas()
print('\n')
get_level_datas()
print('\n')
get_fan_datas()
print('\n')
get_fan_sorting_datas()
