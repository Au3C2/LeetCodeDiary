'''
Description: 
Autor: Au3C2
Date: 2021-10-09 19:07:42
LastEditors: Au3C2
LastEditTime: 2021-10-09 19:17:32
'''
nums = [1,1,1,2,2,2,3,3,3,3]
ans = set()
def recursion(nums, s):
    global ans
    if not nums:
        ans.add(s)
        return
    for i, n in enumerate(nums):
        s += str(nums[i])
        recursion(nums[:i]+nums[i+1:], s)
        s = s[:-1]
recursion(nums, '')
print(len(ans))