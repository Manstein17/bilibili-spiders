import matplotlib
from matplotlib import pyplot as plt


def upload_data():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(6, 6))
    plt.title("用户活跃数据")
    labels = [u'up主', u'观众']
    sizes = [999937-831777, 831777]
    colors = ['red', 'yellowgreen']
    plt.pie(sizes,
            labels=labels,
            colors=colors,
            autopct='%3.2f%%',
            startangle=90,
            pctdistance=0.6)
    plt.axis('equal')
    plt.show()


def sex_data():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(6, 6))
    plt.title("用户性别数据")
    labels = [u'男', u'女', u'保密']
    sizes = [210262, 66120, 723555]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.pie(sizes,
            labels=labels,
            colors=colors,
            autopct='%3.2f%%',
            startangle=90,
            pctdistance=0.6)
    plt.axis('equal')
    plt.show()


def vip_data():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(6, 6))
    plt.title("用户VIP数据")
    labels = [u'年费会员', u'月度会员', u'非会员']
    sizes = [216811, 570692, 212434]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.pie(sizes,
            labels=labels,
            colors=colors,
            autopct='%3.2f%%',
            startangle=90,
            pctdistance=0.6)
    plt.axis('equal')
    plt.show()


def level_data():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    users = [175019, 125142, 68111, 59729, 129270, 394189, 48477]
    plt.barh(range(7), users, height=0.7, color='steelblue')
    plt.yticks(range(7), ['LV0', 'LV1', 'LV2', 'LV3', 'LV4', 'LV5', 'LV6'])
    plt.xlim(0, 500000)
    plt.xlabel("人数")
    plt.title("用户等级数据")
    for x, y in enumerate(users):
        plt.text(y, x, '%s' % y)
    plt.show()


def fans_data():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    users = [568046, 303696, 89455, 27369, 8747, 2159, 416, 48, 1]
    plt.barh(range(9), users, height=0.7, color='steelblue')
    plt.yticks(range(9), ['粉丝数为0', '个级', '十级', '百级', '千级', '万级',
                          '十万级', '百万级', '千万级'])
    plt.xlim(0, 600000)
    plt.xlabel("用户数")
    plt.title("用户拥有粉丝数据")
    for x, y in enumerate(users):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    plt.show()

upload_data()
sex_data()
vip_data()
level_data()
fans_data()
