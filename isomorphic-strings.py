class Solution:
    def isIsomorphic(self, s, t):
        len_set = set(zip(s, t))
        return len(len_set) == len(set(s)) == len(set(t))