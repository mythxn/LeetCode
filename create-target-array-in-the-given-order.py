class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for value, ind in zip(nums, index):
            target.insert(ind, value)
        return target