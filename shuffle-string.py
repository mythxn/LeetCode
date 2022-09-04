class Solution:
    def restoreString(self, s, indices):
        res = [None] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(res)
