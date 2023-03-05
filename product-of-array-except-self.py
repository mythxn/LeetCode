from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate the product of all elements to the left of each element
        left_products = [1] * len(nums)
        for i in range(1, len(nums)):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate the product of all elements to the right of each element
        right_products = [1] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Calculate the final product except self using left and right products
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left_products[i] * right_products[i]

        return result
