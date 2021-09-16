'''
Description: 百度笔试1
Autor: Au3C2
Date: 2021-09-14 19:44:13
LastEditors: Au3C2
LastEditTime: 2021-09-15 11:08:22
'''
'''
5
20 5
30 10
25 8
15 15
10 6
'''
import heapq

n = int(input().strip())
tasks = []
for _ in range(n):
    deadline, points = input().strip().split(' ')
    tasks.append((int(deadline), int(points)))
tasks.sort(key = lambda x: x[0])
maxHeap = []

time = 0
for deadline, points in tasks:
    time += 10
    heapq.heappush(maxHeap, points)

    if time > deadline:
        heapq.heappop(maxHeap)
        time -= 10

print(sum(maxHeap))