class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        r = prices[0]
        for price in prices:
            if price < r:
                r = price
            profit = max(profit, price-r)
        return profit