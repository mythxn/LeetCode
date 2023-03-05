from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize the minimum price to the maximum possible value 
        # and the maximum profit to 0.
        min_price = float('inf')
        max_profit = 0

        # Iterate through each price in the list.
        for price in prices:
            # If the current price is less than the minimum price, update the minimum price.
            if price < min_price:
                min_price = price
            # If the difference between the current price and the minimum price
            # is greater than the maximum profit, update the maximum profit.
            elif price - min_price > max_profit:
                max_profit = price - min_price

        # Return the maximum profit.
        return max_profit
