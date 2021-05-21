#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        out = 0
        for num in nums:
            out ^= num
        return out


# @lc code=end
