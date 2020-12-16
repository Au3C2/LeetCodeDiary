'''
Description: 
Autor: Au3C2
Date: 2020-12-14 09:59:21
LastEditors: Au3C2
LastEditTime: 2020-12-14 10:01:04
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            # key = "".join(sorted(st))
            mp["".join(sorted(st))].append(st)
        return list(mp.values())

# 哈希表
# 将排序后的字符串当作键
# https://leetcode-cn.com/problems/group-anagrams/
# https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/