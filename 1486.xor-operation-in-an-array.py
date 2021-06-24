#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums, xor = [start + 2 * i for i in range(n)], 0

        for num in nums:
            xor ^= num

        return xor


# @lc code=end
