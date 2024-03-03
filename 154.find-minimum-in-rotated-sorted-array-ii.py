#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[r]:
                r -= 1
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]
# @lc code=end

