class NumArray:
    def __init__(self, nums):
        self.running_total = [0]

        self.running_total.extend(
            el + self.running_total[idx] for idx, el in enumerate(nums)
        )

    def sumRange(self, left, right):
        return self.running_total[right + 1] - self.running_total[left]
