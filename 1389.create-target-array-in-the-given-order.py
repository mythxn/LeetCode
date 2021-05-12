#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for value, ind in zip(nums, index):
            target.insert(ind, value)
        return target


# @lc code=end
