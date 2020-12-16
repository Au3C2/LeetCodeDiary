'''
Description: 
Autor: Au3C2
Date: 2020-12-15 11:04:55
LastEditors: Au3C2
LastEditTime: 2020-12-15 11:08:57
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        max_points = now_points = sum(cardPoints[:k])
        for i in range(k):
            now_points = now_points - cardPoints[k-i-1] + cardPoints[-1-i]
            max_points = max(max_points,now_points)
        return max_points

# 滑窗
# 我的想法正好是 https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/solution/ 的相反，
# 也就是说我是正向思维，遍历所有情况。初始化窗口，该窗口为挑选的所有卡。从全部挑选最左边卡开始，然后弹出窗口内最右端点数，
# 加入cardPoints末尾的1个数字