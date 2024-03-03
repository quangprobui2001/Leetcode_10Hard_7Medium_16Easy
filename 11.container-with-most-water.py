#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        s, e = 0, len(height) - 1
        while s < e:
            l = e - s
            h = min(height[s], height[e])
            m = max(0, l * h)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return m
# @lc code=end

