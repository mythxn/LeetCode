#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]
        part_idx = 0

        for i in range(1, len(nums)):
            if local_max > nums[i]:
                local_max = global_max
                part_idx = i
            else:
                global_max = max(global_max, nums[i])

        return part_idx + 1

# @lc code=end
