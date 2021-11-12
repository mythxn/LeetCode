#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        count_dict = {}
        for i, val in enumerate(nums):
            count_dict[val] = count_dict.get(val, 0) + 1

        return [x for x in count_dict if count_dict[x] == 1]

# @lc code=end
