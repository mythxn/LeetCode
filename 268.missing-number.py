#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        exp_sum = (1 + n) * n // 2
        act_sum = sum(nums)
        return exp_sum - act_sum


# @lc code=end
