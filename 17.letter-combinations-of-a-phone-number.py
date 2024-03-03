#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char = {"2":"abc",
               "3": "def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7": "qprs",
               "8":"tuv",
               "9":"wxyz"
               } 
        #viet ham backtracking
        def backtrack(i, curStr):# i: cho biết đang ở chỉ mục nào trong chuỗi chữ số
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in char[digits[i]]:
                backtrack(i + 1, curStr + c)

               #Hàm này kiểm tra điều kiện dừng là độ dài của curStr
                #bằng với độ dài của digits (nghĩa là, đã tạo ra một kết hợp hoàn chỉnh)
                #và sau đó thêm curStr vào res. Nếu chưa đạt điều kiện dừng, 
                #hàm sẽ lặp qua mỗi chữ cái tương ứng với chữ số hiện tại (digits[i]), 
                #và gọi đệ quy chính nó với chỉ số tiếp theo và chuỗi hiện tại được nối thêm chữ cái đang xét.'''
        if digits:
            backtrack(0, "")
        return res
       
# @lc code=end

