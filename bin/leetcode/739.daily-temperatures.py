#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        for day, day_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < day_temp:
                i = stack.pop()
                answer[i] = day - i
            stack.append(day)

        return answer


# @lc code=end

