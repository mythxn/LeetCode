#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        dict = {}
        result = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]] = i

        for i in range(len(nums)):
            result.append(dict[nums[i]])

        return result


# @lc code=end
