#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s, indices):
        res = [None] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(i for i in res)


# @lc code=end
