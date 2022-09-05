class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed += [nums[i + 1]] * nums[i]
        return decompressed