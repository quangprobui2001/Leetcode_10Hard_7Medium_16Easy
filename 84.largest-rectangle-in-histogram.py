#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights): # enumrate cho phép lặp qua 1 danh sách và trả về cả index và value tương ứng
            start = i
            while stack and stack[-1][1] > h:# lặp đến khi stack rỗng và chiều cao của ptu cuoi trong stack lớn hơn h hiện tại
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
# @lc code=end

