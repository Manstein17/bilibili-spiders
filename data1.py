import pandas as pd
import pymysql

## 加上字符集参数，防止中文乱码
dbconn=pymysql.connect(
  host="localhost",
  database="test",
  user="root",
  password="",
  port=3306,
  charset='utf8'
 )

#sql语句
sqlcmd = "select name, sex, attention, level, vipType from users limit 10"

#利用pandas 模块导入mysql数据
a = pd.read_sql(sqlcmd,dbconn)
#取前5行数据
b = a.head(572)
print(b)



# 读取csv数据
# pd.read_csv()

# 读取excel数据
#pd.read_excel()

# 读取txt数据
#pd.read_table()
