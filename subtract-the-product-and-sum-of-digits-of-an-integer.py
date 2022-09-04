import math


class Solution:
    def subtractProductAndSum(self, n):
        list = [int(x) for x in str(n)]
        return math.prod(list) - sum(list)
