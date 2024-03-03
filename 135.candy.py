#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_children = len(ratings)
        candies_from_left = [1] * num_children
        candies_from_right = [1] * num_children
      
        for i in range(1, num_children): 
            if ratings[i] > ratings[i - 1]:
                candies_from_left[i] = candies_from_left[i - 1] + 1
      
        for i in range(num_children - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_from_right[i] = candies_from_right[i + 1] + 1
    
        total_candies = sum(max(candies_left, candies_right) for candies_left, candies_right in zip(candies_from_left, candies_from_right))
      
        return total_candies
# @lc code=end

