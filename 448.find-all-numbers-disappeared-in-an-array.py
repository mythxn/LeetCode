#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        for i in nums:
            pos = abs(i) - 1  # -1 to get indices
            nums[pos] = abs(nums[pos]) * -1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# @lc code=end
