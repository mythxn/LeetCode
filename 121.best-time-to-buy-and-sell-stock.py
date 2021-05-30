#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, sell_price = 0, 1
        maxProfit = 0

        while sell_price < len(prices):
            # if profitable, check if max profit
            if prices[sell_price] > prices[buy_price]:
                profit = prices[sell_price] - prices[buy_price]
                maxProfit = max(maxProfit, profit)
            # else, new buy price as its cheaper
            else:
                buy_price = sell_price
                
            sell_price += 1
        return maxProfit


# @lc code=end
