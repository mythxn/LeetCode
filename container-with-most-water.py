class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize pointers at both ends of the list of heights
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Continue iterating until the pointers meet
        while left < right:
            # Calculate the area between the two pointers
            area = min(height[left], height[right]) * (right - left)
            # If this area is greater than the maximum area seen so far, update max_area
            if area > max_area:
                max_area = area
            # Move the pointer that corresponds to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
