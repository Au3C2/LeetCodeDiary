'''
Description: 
Autor: Au3C2
Date: 2021-02-14 11:59:35
LastEditors: Au3C2
LastEditTime: 2021-02-14 12:00:29
'''
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int: # 暴力解，异或运算
        result = 0
        for i in range(0, len(row), 2):
            if row[i] == row[i + 1] ^ 1: # 运用异或运算判断是不是一对情侣
                continue
            for j in range(i + 2, len(row), 1): # 如果不是，再进行搜寻
                if row[j] ^ 1 == row[i]: # 搜到了，那么接下来进行座位交换
                    row[i + 1], row[j] = row[j], row[i + 1]
                    result += 1 # 交换次数+1
                    break
        return result # 得到总的交换次数

# 并查集，贪心，困难。单身程序员的无能狂怒。
# 所以为啥暴力搜索能过呢？
# https://leetcode-cn.com/problems/couples-holding-hands/