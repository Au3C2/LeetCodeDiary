<!--
 * @Description: 华为0825题3
 * @Autor: Au3C2
 * @Date: 2021-08-25 20:00:50
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-08-26 11:34:11
-->

```python
from collections import *
import sys

n = int(input().strip())
G = defaultdict(set)
inG = defaultdict(int)
cost = defaultdict(int)
all_cost = 0
for i in range(n):
    line = input().strip().split(' ')
    cost[i] = int(line[1])
    all_cost += cost[i]
    if line[0] != '-1':
        for j in line[0].split(','):
            j = int(j)
            G[j].add(i)
            inG[i] += 1
q = deque()
for i in range(n):
    if not inG[i]:
        q.append(i)
t_cost = 0
done = set()
while q:
    max_cost = 0
    for _ in range(len(q)):
        cur = q.popleft()
        max_cost = max(cost[cur],max_cost)
        done.add(cur)
        for j in G[cur]:
            inG[j] -= 1
            if not inG[j]:
                q.append(j)
    t_cost += max_cost

print(t_cost if len(done) == n else -1)
```