<!--
 * @Description: 华为0825题1
 * @Autor: Au3C2
 * @Date: 2021-08-18 23:11:32
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-08-26 11:34:29
-->

```python
import collections
import sys

# pin = sys.stdin.readlines()
line = input().strip().split(' ')
m, n = int(line[0]), int(line[1])
matrix = []
for i in range(m):
    line = input().strip().split(' ')
    line = [int(num) for num in line]
    matrix.append(line)
# print(matrix)
ans = 0
for i in range(m):
    sum_row = [0] * n 
    for j in range(i,m):
        for q in range(n): 
            sum_row[q] += matrix[j][q]
        temp = sum_row[0]
        t_ans = sum_row[0]
        for k in range(1,n):
            temp= max(temp+sum_row[k],sum_row[k])
            t_ans = max(temp,t_ans)
        ans = max(t_ans,ans)
print(ans)
```