from typing import List


class Solution:
    def ecrypt(self, x):
        return int(str(max([*str(x)])) * len(str(x)))
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        max_num = sum([self.ecrypt(x) for x in nums])
        return max_num

print(Solution().sumOfEncryptedInt([32,23, 45]))