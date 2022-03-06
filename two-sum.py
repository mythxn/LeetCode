class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val: idx

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[val] = idx