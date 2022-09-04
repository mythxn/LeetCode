class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_p, sell_p = 0, 1
        max_profit = 0

        while sell_p < len(prices):
            profit = prices[sell_p] - prices[buy_p]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy_p = sell_p
            sell_p += 1

        return max_profit