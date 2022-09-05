class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        full_nums = list(range(1, len(nums) + 1))
        return set(nums) ^ set(full_nums)
