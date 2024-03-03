#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#

# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest // minutesToDie + 1
        res, p = 0, 1
        while p < buckets:
            p *= base
            res += 1
        return res
# @lc code=end

