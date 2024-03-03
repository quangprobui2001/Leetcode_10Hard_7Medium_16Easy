#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            n = abs(n)
            return self.myPow(1/x, n)
        elif n % 2 == 0:
            return self.myPow(x * x, n//2)
        else :
            return x * self.myPow(x * x, n // 2 )
# @lc code=end

