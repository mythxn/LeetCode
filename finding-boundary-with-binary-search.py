class Solution:
    def find_boundary(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr[0] == 0:
            return 0
        if arr[-1] == 1:
            return len(arr)
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == 0:
                left = mid + 1
            else:
                right = mid
        return left