#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
import math


class Solution:
    def subtractProductAndSum(self, n):
        list = [int(x) for x in str(n)]
        return math.prod(list) - sum(list)


# @lc code=end
