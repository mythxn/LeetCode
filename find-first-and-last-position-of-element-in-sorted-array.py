class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, "left")
        right = self.binSearch(nums, target, "right")

        return [left, right]

    # if leftBias false; res is rightBias
    def binSearch(self, nums, target, bias):
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if bias == "left":
                    r = m - 1
                elif bias == "right":
                    l = m + 1
        return i
