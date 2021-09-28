'''
Description: 
Autor: Au3C2
Date: 2021-09-26 20:34:33
LastEditors: Au3C2
LastEditTime: 2021-09-27 16:41:59
'''
'''
4
4 7
5 6
10 9
100 9

'''
import numpy as np
"""
集齐十二生肖卡问题：某餐厅开展集齐十二生肖卡活动，顾客每消费一次，
随机发给一张生肖卡。如果顾客集齐十二生肖卡，则可以免费消费一次。编写Python代码，
应用蒙特卡罗方法（Monte Carlo Method）来估计平均消费多少次可以集齐十二生肖卡。
"""
def ran_number(a,b):
    k = 0
    c=[]
    for i in range(0,12):# range左闭右开
        c.append(np.random.randint(a, b))# 先添加十二张卡
    for i in range(0,100):
        d = np.unique(c)# 算出c数组里面不重复的个数有多少
        if len(d)==12: # 如果不重复个数为12，则说明已经筹集到十二张生肖卡
            k=i+12
            print(k)
            break
        else:
           c.append(np.random.randint(a, b)) 
    return k# 返回此次实验的总共消费了多少次

n=[]
for j in range(0,2000): # 进行2000次实验
    n.append(ran_number(0,12))# 12张卡片0，1，2，3，4，5，6，7，8，9，10，11，添加每次实验的消费次数
print(type(n))
mean=sum(n)/2000 #平均一次实验需要消费多少次
print(mean)