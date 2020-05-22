list = [1,2,3,4,5,6,7,5,4,3,2,12]
set  = set(list)
dict = {}

for item in set:
    dict.update({item:list.count(item)})

print(dict)



plt.figure(figsize=(6,9)) #调节图形大小
labels = [u'非会员',u'月会员',u'年费会员'] #定义标签
x = get_datas()
for sizes in x:
    sizes = [] #每块值

colors = ['red','yellowgreen','lightskyblue','yellow'] #每块颜色定义
explode = (0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.show()
