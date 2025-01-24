#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleMap = {}
        for n in nums:
            if n in singleMap:
                singleMap.pop(n)
            else:
                singleMap[n] = 1
        return singleMap.popitem()[0]
# @lc code=end

