#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        missing = []

        for i in nums:
            pos = abs(i) - 1  # -1 to get indices
            nums[pos] = abs(nums[pos]) * -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)  # +1 back to pos

        return missing


# @lc code=end
