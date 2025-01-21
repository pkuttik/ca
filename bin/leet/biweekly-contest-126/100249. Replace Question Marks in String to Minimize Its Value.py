class Solution:
    MIN_VALUE = 0
    INPUT_STR = ''
    MIN_COST = 0
    def cost(self, iChar, i):
        cost_i = 0
        for j in range(0, i):
            if self.INPUT_STR[j] == iChar:
                cost_i += 1
        return cost_i

    def minimizeStringValue(self, s: str) -> str:
        self.INPUT_STR = s
        replace_char_count = s.count('?')
        print(replace_char_count)
        replacement_list = []
        for i in range(97, 97 + 26):
            replacement_char = chr(i)
            if replacement_char not in s:
                replacement_list.append(replacement_char)
            # print(replacement_char, replacement_list)
            if len(replacement_list) == replace_char_count:
                break
        total_cost = 0
        # for i in range(0, len(s)):
        #     total_cost += self.cost(s[i], i)
        for x in replacement_list:
            self.INPUT_STR = self.INPUT_STR.replace('?', x, 1)

        return self.INPUT_STR


print(Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
