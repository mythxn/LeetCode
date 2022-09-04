class Solution:
    def first_not_smaller(self, arr, target):
        left, right = 0, len(arr) - 1
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return boundary_index

    def find_first_occurrence(self, arr, target):
        self.first_not_smaller(arr, target)
