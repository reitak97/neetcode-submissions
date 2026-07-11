class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for n in prices:
            res = max(res, n-curr)
            if n < curr:
                curr = n
        return res