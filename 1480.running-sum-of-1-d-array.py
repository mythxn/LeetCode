#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums


# @lc code=end
