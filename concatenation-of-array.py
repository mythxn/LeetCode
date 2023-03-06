from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)  # get length of input array nums
        ans = [0] * (2 * n)  # create ans array with twice the length of nums

        # copy each element of nums to corresponding position in ans
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans  # return the concatenated array
