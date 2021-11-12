#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number(self, num):
        sanitized_num = list(str(num))
        for i, val in enumerate(sanitized_num):
            if val != '9':
                sanitized_num[i] = '9'
        return ''.join(sanitized_num)

# @lc code=end
