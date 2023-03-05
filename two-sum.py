from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers 'nums' and an integer 'target', return
        indices of the two numbers such that they add up to 'target'. You may
        assume that each input would have exactly one solution, and you may not
        use the same element twice. You can return the answer in any order.
        """
        # Create a dictionary to store the difference between target and the
        # current element
        diff_dict = {}

        # Loop through each element in the list
        for i in range(len(nums)):
            # If the difference between the target and the current element is
            # already in the dictionary, we've found our pair
            if nums[i] in diff_dict:
                # Return the indices of the current element and the element
                # whose difference is in the dictionary
                return [diff_dict[nums[i]], i]
            else:
                # Add the difference between the target and the current element
                # to the dictionary with its index
                diff_dict[target - nums[i]] = i
