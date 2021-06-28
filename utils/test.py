'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-28 16:00:04
'''
import collections
import heapq
from collections import defaultdict, deque
from functools import *
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
from typing import *
import copy
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stations = defaultdict(set)
        for i, route in enumerate(routes):
            for station in route:
                    stations[station].add(i)
        if not stations[source] or not stations[target]:
            return -1
        routes = [set(x) for x in routes]
        
        queue = deque([source]) # cur_station, last_route, step
        visited_s = {source} # 记录到过的站点
        visited_r = set() # 记录乘过的巴士
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur_station = queue.popleft()
                for next_route in stations[cur_station] - visited_r: # 遍历能乘坐的线路
                    for next_station in routes[next_route] - visited_s:
                        if next_station == target:
                            return step + 1
                        queue.append(next_station)
                        visited_s.add(next_station)
                    visited_r.add(next_route)
            step += 1
        return -1
        pass
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        # s2r[station_id]=[route_0,route_1,...,route_k] ，记录站点有哪些公交线路
        s2r = defaultdict(list) # 带default的字典类，元素为list
        for route_id,route in enumerate(routes):    # 遍历每条线路
            for station_id in route:    # 记录每个站点有哪些线路经过
                s2r[station_id].append(route_id)
        graph=[set() for route_i in range(len(routes))] # 线路之间邻接图
        for adj_routes in filter(lambda l:len(l)>1,s2r.values()):   # 遍历每个站点经过的线路（筛选至少有两条线路的）
            for i,route_i in enumerate(adj_routes):     # 相邻线路之间构造邻接表
                graph[route_i]|=set(adj_routes[:i]+adj_routes[i+1:]) # python的set类， | 代表并集运算
        # BFS
        ans=0
        target_routes=set(s2r[target])  # 终点站所经过的线路集合
        queue=set(s2r[source])  # 队列初始化为起点站所经过的线路集合
        visit=set() #已经遍历过的线路集合（每一条线路至多只遍历一次）
        while queue:
            ans+=1 # 坐公交就要+1
            if len(queue&target_routes)>0:return ans    #与 target 在同一条线路上
            queue2=set()    # 后继节点集合，
            for route_i in queue:   # 先求所有与queue中线路相邻的线路
                queue2|=graph[route_i]  # | 是并集运算
            visit |= queue  # 记录已经visit的
            queue=queue2-visit  # 因为与queue中线路相邻的包含已经visit过的，故要做差集去掉。
        return -1   #无法到达target
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
