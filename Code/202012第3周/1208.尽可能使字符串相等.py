class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost=0
        n=len(s)
        i=0
        res=0
        for j in range(n): # 右指针遍历
            cost+=abs(ord(s[j])-ord(t[j]))
            while cost>maxCost:
                cost-=abs(ord(s[i])-ord(t[i]))
                i+=1 # 左指针前进1位
            res=max(res,j-i+1)
        return res
    
# 计算出两字符串差，那么问题就转换为寻找字串和小于maxCount的最长字串
# 是个滑窗问题
# https://leetcode-cn.com/problems/get-equal-substrings-within-budget/