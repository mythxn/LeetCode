class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p, sell_p = 0, 1
        max_profit = 0

        while sell_p < len(prices):
            if prices[buy_p] < prices[sell_p]:
                cur_profit = prices[sell_p] - prices[buy_p]
                max_profit = max(max_profit, cur_profit)
            else:
                buy_p = sell_p
            sell_p += 1

        return max_profit