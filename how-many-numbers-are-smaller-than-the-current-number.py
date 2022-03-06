class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        dict = {}
        result = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]] = i

        for i in range(len(nums)):
            result.append(dict[nums[i]])

        return result