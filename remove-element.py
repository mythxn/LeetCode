from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # If the input list is empty, return 0
        if not nums:
            return 0
        
        # Initialize a pointer i to keep track of the index of the next non-val element
        i = 0
        
        # Iterate through the input list using a pointer j
        for j in range(len(nums)):
            # If the j-th element is not val, copy it to the i-th position and increment i
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        # The new length of the array is i
        return i
