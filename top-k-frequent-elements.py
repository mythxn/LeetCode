from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count the frequency of each number using Counter
        counter = Counter(nums)

        # Step 2: Sort the numbers by their frequency in descending order
        sorted_nums = sorted(counter, key=lambda x: counter[x], reverse=True)

        # Step 3: Return the first k elements of the sorted list
        return sorted_nums[:k]
