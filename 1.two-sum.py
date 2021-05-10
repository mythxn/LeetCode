#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for el in nums:
            el_index = nums.index(el)  # store index
            unvisited = nums[:el_index] + nums[el_index + 1 :]  # unvisited list
            nums[el_index] = "x"  # mark as visited

            if target - el in unvisited:
                return [el_index, nums.index(target - el)]


# @lc code=end
