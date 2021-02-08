'''
Description: 
Autor: Au3C2
Date: 2021-02-08 10:26:40
LastEditors: Au3C2
LastEditTime: 2021-02-08 10:34:49
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if len(set(arr)) == 1:
            return 1
        if n == 2:
            return 2

        change = []
        for i in range(n-2):
            if arr[i] < arr[i+1] and arr[i+1] > arr[i+2] or \
                arr[i] > arr[i+1] and arr[i+1] < arr[i+2]:
                change.append(-1)
            elif arr[i] == arr[i+1] or arr[i+1] == arr[i+2]:
                change.append(0)
            else:
                change.append(1)

        i = 0
        max_len = 0
        while i < n-2 :
            if change[i] == -1:
                j = i + 1
                for j in range(i+1,n-2):
                    if change[j] != -1:
                        j -= 1
                        break
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                i = j
            i += 1
        return max_len + 2
    
# 数组，中等。又是做过的题
# https://leetcode-cn.com/problems/longest-turbulent-subarray/
    
