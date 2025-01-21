#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer: List[List[int]] = []
        input_size = range(len(nums))
        for i in input_size:
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                for k in range(j+1, len(nums)):
                    if j == k or i == k:
                        continue
                    # print(i, j, k)
                    if nums[i] + nums[k] + nums[j] == 0:
                        s = sorted([nums[i], nums[j], nums[k]])
                        if s not in answer:
                            answer.append(s)
        return answer
        
# @lc code=end

