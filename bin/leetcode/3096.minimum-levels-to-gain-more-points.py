#
# @lc app=leetcode id=3096 lang=python3
#
# [3096] Minimum Levels to Gain More Points
#

# @lc code=start
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        # possible = [1 if x == 1 else -1 for x in possible]
        # win, score = sum(possible) // 2, 0
        # for i, turn in enumerate(possible[:-1]):
        #     score += turn
        #     # print(score, win)
        #     if score > win:
        #         return i + 1
        # return -1
        prefix_sum = [0]
        s = len(possible)
        for i in range(s):
            prefix_sum.append(prefix_sum[i] + (1 if possible[i] == 1 else -1))
        # print(prefix_sum)
        total_score = prefix_sum[s]
        for i in range(s-1):
            # print(i, p1_score, p2_score)
            if prefix_sum[i+1] > (total_score - prefix_sum[i+1]):
                return i + 1
        return -1
# @lc code=end

