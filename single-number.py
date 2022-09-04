class Solution:
    def singleNumber(self, nums):
        out = 0
        for num in nums:
            out ^= num
        return out
