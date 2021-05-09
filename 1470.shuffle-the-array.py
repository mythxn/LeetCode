#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr_1 = nums[:n]
        arr_2 = nums[n::]
        out = []

        for el in range(n):
            out.append(arr_1[el])
            out.append(arr_2[el])

        return out


# @lc code=end
