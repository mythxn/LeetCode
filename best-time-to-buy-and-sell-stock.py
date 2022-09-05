class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            cur_profit = price - min_price
            if price < min_price:
                min_price = price
            elif cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit