<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-07-30 16:45:50
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-07-31 15:11:41
-->
利用拓扑排序即可

```python

import collections
import sys

# 读取数据
pin = sys.stdin.readlines()
m = int(pin[0].strip())
n = int(pin[1].strip())
z = int(pin[2].strip())
depend = list()  # depend 列表
for i in range(3, 3+z):
    depend.append([int(j) for j in pin[i].strip().split(' ')])

# print(m, n, z, depend)

# 药依赖字典， 以 被依赖的药：[药1， 药2].。的方式存
edge = collections.defaultdict(list)
# 药依赖次数字典， 以 药：依赖次数。。的方式存
depend_num = collections.defaultdict(int)
for i in depend:
    edge[i[0]].append(i[1])
    depend_num[i[0]]
    depend_num[i[1]] += 1

# print(edge, depend_num)

day = 0

# 队列初始化，将能喝的药放入队列中
queue = queue.dequeue()
for k, v in depend_num.items():
    if v == 0:
        queue.append(k)

# print(queue)

day = 0
while queue:
    len_ = len(queue)
    for _ in range(min(n, len_)):  # 喝上当天最多能喝的数量:
        tmp = queue.popleft()
        for j in edge[tmp]:
            depend_num[j] -= 1
            if depend_num[j] == 0: # 此刻该药的所有依赖药都吃了，因此这药能吃，送入队列
                queue.append(j)
    day += 1

print(day)
```