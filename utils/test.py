'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-08 16:52:55
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
from itertools import *
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        presum = [0] + list(accumulate(nums))
        # hashmap = defaultdict(int, {0:1})
        hashmap = Counter([0])
        ans = 0
        for i in range(n):
            r = presum[i+1]
            # if r < goal:
            #     break
            l = r - goal
            ans += hashmap[l]
            hashmap[r] += 1
        return ans
        
        # 暴力搜索超时
        # for i in range(n):  
        #     for j in range(i+1,n+1):
        #         d = pre_sum[j] - pre_sum[i]
        #         if d > goal:
        #             break
        #         if d == goal:
        #             ans += 1
        
        # 滑动窗口写不来
        # lp, rp = 0, 0
        # w = nums[0] # 记录窗口和

        # while w != goal: # 初始化窗口
        #     rp += 1
        #     w += nums[rp]
        # ans = 1
        # while lp < n-1:
        #     while w == goal and rp < n-1:
        #         rp += 1
        #         w += nums[rp]
        #         ans += 1
        #     # rp -= 1
        #     # w -= nums[rp]
        #     # ans -= 1

        #     lp += 1
        #     w -= nums[lp]

        # return ans
        
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function([1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0], 3)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
