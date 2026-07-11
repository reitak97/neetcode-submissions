class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = prices[0]
        for price in prices:
            if price < l:
                l = price
            profit = max(profit, price-l)

        return profit