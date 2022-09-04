class Solution:
    def singleNumber(self, nums):
        count_dict = {}
        for val in nums:
            count_dict[val] = count_dict.get(val, 0) + 1

        return [x for x in count_dict if count_dict[x] == 1]
