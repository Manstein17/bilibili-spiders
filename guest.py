# Python-
用于存储0基础学习Python中所经历的代码
guest = input(str('请输入您的名字用于登记：'))

file = 'guest.txt'
with open(file,'a') as j:
    j.write(guest.title())
    j.write('\n')

print('谢谢合作')
