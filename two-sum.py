class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping_dict = {}  # val: idx
        for i, v in enumerate(nums):
            diff = target - v
            if diff in mapping_dict:
                return [mapping_dict[diff], i]
            else:
                mapping_dict[v] = i
