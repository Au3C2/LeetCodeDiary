'''
Description: 
Autor: Au3C2
Date: 2021-01-31 15:08:50
LastEditors: Au3C2
LastEditTime: 2021-02-01 18:46:34
'''
'''
Description: 
Autor: Au3C2
Date: 2021-01-26 14:50:22
LastEditors: Au3C2
LastEditTime: 2021-01-26 14:50:33
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dc = collections.defaultdict(int)
        for d in dominoes:
            if d[0] > d[1]:
                t = d[0]
                d[0] = d[1]
                d[1] = t
            dc['%d%d'%(d[0],d[1])] += 1
        ans = 0
        for _,value in dc.items():
            if value >= 2: 
                ans += comb(value,2)
        return int(ans)

# 数组，简单，每日一题
# https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/