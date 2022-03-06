class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hi = len(nums)
        lo = 0

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo