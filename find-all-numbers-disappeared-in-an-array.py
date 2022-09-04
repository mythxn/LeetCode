class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_nums = list(range(1, len(nums) + 1))
        return set(nums) ^ set(full_nums)
