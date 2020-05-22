import requests
import jsonpath
import json
import time
import mysql.connector
from multiprocessing import Pool
import random
import linecache
import datetime


def UA():
    a = random.randrange(1, 899)
    ua = linecache.getline(r'user_agents.txt', a)
    return ua.rstrip()


def PR():
    b = random.randrange(1, 103)
    pr = linecache.getline(r'proxies.txt', b)
    return pr.rstrip()


def bilibili_url(mid1):
    url = 'https://api.bilibili.com/x/web-interface/card?mid=' + str(mid1) + '&jsonp=jsonp&article=true'
    return url


def get_user_json(url):
    head = {'User-Agent': UA()}
    proxies = {"http": PR()}
    response = requests.get(url=url, headers=head)
    response.raise_for_status()
    s = requests.session()
    s.keep_alive = False
    return response.content.decode()


def spider1():
    mid_list = list(range(1, 10001))
    for mid1 in mid_list:
        url = bilibili_url(mid1)
        j = get_user_json(url)
        data = json.loads(j)
        code = jsonpath.jsonpath(data, '$..code')
        if code[0] == -404:
            print('该用户已注销')
        else:
            mid = jsonpath.jsonpath(data, '$..mid')
            name = jsonpath.jsonpath(data, '$.data.card.name')
            sex = jsonpath.jsonpath(data, '$..sex')
            fans = jsonpath.jsonpath(data, '$..fans')
            attention = jsonpath.jsonpath(data, '$..attention')
            current_level = jsonpath.jsonpath(data, '$..current_level')
            vipType = jsonpath.jsonpath(data, '$..vipType')
            archive_count = jsonpath.jsonpath(data, '$..archive_count')
            conn = mysql.connector.connect(user='root', password='', database='python_db')
            mycursor = conn.cursor()
            sql = "INSERT INTO users ( mid, name, sex, fans, attention, level, vipType, upload) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = [
                (mid[0], name[0], sex[0], fans[0], attention[0], current_level[0], vipType[0], archive_count[0]),
            ]
            mycursor.executemany(sql, val)
            conn.commit()
            print(mid[0], "记录插入成功。一")
        print(datetime.datetime.now())
        time.sleep(0.2)


def spider2():
    mid_list = list(range(10001, 20001))
    for mid1 in mid_list:
        url = bilibili_url(mid1)
        j = get_user_json(url)
        data = json.loads(j)
        code = jsonpath.jsonpath(data, '$..code')
        if code[0] == -404:
            print('该用户已注销')
        else:
            mid = jsonpath.jsonpath(data, '$..mid')
            name = jsonpath.jsonpath(data, '$.data.card.name')
            sex = jsonpath.jsonpath(data, '$..sex')
            fans = jsonpath.jsonpath(data, '$..fans')
            attention = jsonpath.jsonpath(data, '$..attention')
            current_level = jsonpath.jsonpath(data, '$..current_level')
            vipType = jsonpath.jsonpath(data, '$..vipType')
            archive_count = jsonpath.jsonpath(data, '$..archive_count')
            conn = mysql.connector.connect(user='root', password='', database='python_db')
            mycursor = conn.cursor()
            sql = "INSERT INTO users ( mid, name, sex, fans, attention, level, vipType, upload) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = [
                (mid[0], name[0], sex[0], fans[0], attention[0], current_level[0], vipType[0], archive_count[0]),
            ]
            mycursor.executemany(sql, val)
            conn.commit()
            print(mid[0], "记录插入成功。二")
        print(datetime.datetime.now())
        time.sleep(0.2)


def spider3():
    mid_list = list(range(20001, 30001))
    for mid1 in mid_list:
        url = bilibili_url(mid1)
        j = get_user_json(url)
        data = json.loads(j)
        code = jsonpath.jsonpath(data, '$..code')
        if code[0] == -404:
            print('该用户已注销')
        else:
            mid = jsonpath.jsonpath(data, '$..mid')
            name = jsonpath.jsonpath(data, '$.data.card.name')
            sex = jsonpath.jsonpath(data, '$..sex')
            fans = jsonpath.jsonpath(data, '$..fans')
            attention = jsonpath.jsonpath(data, '$..attention')
            current_level = jsonpath.jsonpath(data, '$..current_level')
            vipType = jsonpath.jsonpath(data, '$..vipType')
            archive_count = jsonpath.jsonpath(data, '$..archive_count')
            conn = mysql.connector.connect(user='root', password='', database='python_db')
            mycursor = conn.cursor()
            sql = "INSERT INTO users ( mid, name, sex, fans, attention, level, vipType, upload) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = [
                (mid[0], name[0], sex[0], fans[0], attention[0], current_level[0], vipType[0], archive_count[0]),
            ]
            mycursor.executemany(sql, val)
            conn.commit()
            print(mid[0], "记录插入成功。三")
        print(datetime.datetime.now())
        time.sleep(0.2)


def spider4():
    mid_list = list(range(30001, 40001))
    for mid1 in mid_list:
        url = bilibili_url(mid1)
        j = get_user_json(url)
        data = json.loads(j)
        code = jsonpath.jsonpath(data, '$..code')
        if code[0] == -404:
            print('该用户已注销')
        else:
            mid = jsonpath.jsonpath(data, '$..mid')
            name = jsonpath.jsonpath(data, '$.data.card.name')
            sex = jsonpath.jsonpath(data, '$..sex')
            fans = jsonpath.jsonpath(data, '$..fans')
            attention = jsonpath.jsonpath(data, '$..attention')
            current_level = jsonpath.jsonpath(data, '$..current_level')
            vipType = jsonpath.jsonpath(data, '$..vipType')
            archive_count = jsonpath.jsonpath(data, '$..archive_count')
            conn = mysql.connector.connect(user='root', password='', database='python_db')
            mycursor = conn.cursor()
            sql = "INSERT INTO users ( mid, name, sex, fans, attention, level, vipType, upload) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = [
                (mid[0], name[0], sex[0], fans[0], attention[0], current_level[0], vipType[0], archive_count[0]),
            ]
            mycursor.executemany(sql, val)
            conn.commit()
            print(mid[0], "记录插入成功。四")
        print(datetime.datetime.now())
        time.sleep(0.2)


if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.apply_async(spider1)
    pool.apply_async(spider2)
    pool.apply_async(spider3)
    pool.apply_async(spider4)

    pool.close()
    pool.join()
