class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        buy = prices[0]
        for p in prices:
            res = max(res, p-buy)
            buy = min(buy,p)

        return res