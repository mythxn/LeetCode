class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest_val = max(candies)
        output = []

        for kid in candies:
            if kid + extraCandies >= highest_val:
                output.append(True)
            else:
                output.append(False)

        return output