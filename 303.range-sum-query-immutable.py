#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:
    def __init__(self, nums):
        self.running_total = [0]

        for idx, el in enumerate(nums):
            self.running_total.append(el + self.running_total[idx])

    def sumRange(self, left, right):
        return self.running_total[right + 1] - self.running_total[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
