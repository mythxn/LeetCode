#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        sum = self.str_to_sum(num)
        while len(str(sum)) != 1:
            sum = self.str_to_sum(sum)
        return sum

    def str_to_sum(self, n: int) -> int:
        string = str(n)
        sum = 0
        for char in string:
            sum += int(char)
        return sum


# @lc code=end
