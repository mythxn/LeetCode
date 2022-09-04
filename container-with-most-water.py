class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l

            area = h * w
            maxArea = max(maxArea, area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxArea
