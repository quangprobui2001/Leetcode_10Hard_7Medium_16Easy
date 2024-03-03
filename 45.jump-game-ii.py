#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res  = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            far = 0
            for i in range(l , r + 1):
                far = max (far, i + nums[i])
            l = r + 1
            r = far
            res += 1
        return res
# @lc code=end

