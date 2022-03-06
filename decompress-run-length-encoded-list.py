class Solution:
    def decompressRLElist(self, nums):
        out = []
        for freq, val in zip(nums[0::2], nums[1::2]):
            for _ in range(freq):
                out.append(val)
        return out