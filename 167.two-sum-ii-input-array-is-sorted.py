#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers) - 1

        while True:
            curSum = numbers[small] + numbers[big]

            if curSum > target:
                big -= 1
            elif curSum < target:
                small += 1
            else:
                return [small + 1, big + 1]


# @lc code=end
