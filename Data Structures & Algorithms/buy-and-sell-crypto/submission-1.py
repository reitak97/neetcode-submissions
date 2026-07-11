class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = prices[0]
        for price in prices:
            if price < l:
                l = price
            maxP = max(maxP, price-l)
        return maxP