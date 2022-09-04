class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr_1 = nums[:n]
        arr_2 = nums[n::]
        out = []

        for el in range(n):
            out.extend((arr_1[el], arr_2[el]))
        return out
