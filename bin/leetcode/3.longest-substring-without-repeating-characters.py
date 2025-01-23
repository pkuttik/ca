#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        longest_string = ""
        for c in s:
            if c in longest_string:
                longest_string = longest_string[longest_string.index(c) + 1:] + c
            else:
                longest_string = longest_string + c
                answer = max(answer, len(longest_string))
        return answer
# @lc code=end

