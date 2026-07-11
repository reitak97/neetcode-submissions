class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxPrice = 0
        for price in prices:
            if price < l:
                l = price
            maxPrice = max(price-l, maxPrice)
        return maxPrice

    
        

       