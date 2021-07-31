'''
Description: 
Autor: Au3C2
Date: 2021-07-30 16:12:41
LastEditors: Au3C2
LastEditTime: 2021-07-30 16:43:57
'''
import sys
# sys.setrecursionlimit(1000000)
# m, n = list(map(int, sys.stdin.readline().strip(' ').strip('\n').strip(' ').split(' ')))
# n = int(sys.stdin.readline().strip(' ').strip('\n').strip(' '))
# z = int(sys.stdin.readline().strip(' ').strip('\n').strip(' '))
m, n = 3, 4

graph = [[1,0,0,0],
         [0,0,0,0],
         [0,0,2,-1]]
walk_n = 1
start, end = [], []
for i in range(m):
    # line = list(map(int, sys.stdin.readline().strip(' ').strip('\n').strip(' ').split(' ')))
    line = graph[i]
    # graph.append(line)
    for j in range(n):
        v = line[j]
        if v == 0:
            walk_n += 1
        elif v == 1:
            start = [i, j]
        elif v == 2:
            end = [i, j]
res = [0]
nex = [[0, 1], [1, 0], [0, -1], [-1, 0]]
book = [[0 for _ in range(n)] for _ in range(m)]


def dfs(x, y, t_walk_n, m, n, walk_n):
    if x == end[0] and y == end[1]:
        if t_walk_n == walk_n:
            res[0] += 1
        return

    book[x][y] = 1
    for k in range(len(nex)):
        newx, newy = nex[k][0]+x, nex[k][1]+y
        if 0 <= newx < m and 0 <= newy < n and \
            book[newx][newy] == 0 and graph[newx][newy] != -1:
            dfs(newx, newy, t_walk_n+1, m, n, walk_n)
    book[x][y] = 0


dfs(start[0], start[1], 0, m, n, walk_n)
print(res[0])
