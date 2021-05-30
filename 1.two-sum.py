#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val: idx

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[val] = idx


# @lc code=end
