'''
Description: 
Autor: Au3C2
Date: 2021-02-12 13:44:56
LastEditors: Au3C2
LastEditTime: 2021-02-12 13:45:19
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1],[1,1]]
        if rowIndex < 2:
            return output[rowIndex]
        lastRow = output[1]
        for n in range(2,rowIndex+1): # 第n行,同时也是该行长度
            row = [1] # 这一行初始化
            for i in range(1,(n+1)//2+1): #因为是对称的仅需跑出一半的值
                row.append(lastRow[i-1]+lastRow[i])
            temp = row[:-1] if (n+1)%2==1 else row[:-2]
            row.extend(temp[::-1])
            lastRow = row
        return row
    
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/pascals-triangle-ii/