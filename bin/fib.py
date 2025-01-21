class Solution:
    def fib(self, x):
        # print(x)
        if x < 2:
            return x
        return self.fib(x - 1) + self.fib(x - 2)

print(Solution().fib(2))
