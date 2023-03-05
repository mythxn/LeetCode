from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the input array is empty, return 0
        if not nums:
            return 0
        
        # Initialize two pointers i and j
        i = 0
        
        # Iterate through the array using pointer j
        for j in range(1, len(nums)):
            # If the element at index j is not equal to the element at index i,
            # it is considered as a new unique element, and it is placed at index i+1
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # Return the length of the new array (+1 because the index starts at 0)
        return i + 1
