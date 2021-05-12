#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums):
        out = []
        for freq, val in zip(nums[0::2], nums[1::2]):
            for _ in range(freq):
                out.append(val)
        return out


# @lc code=end
