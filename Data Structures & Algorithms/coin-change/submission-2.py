class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for t in range(1,amount+1):
            for c in coins:
                if t-c >=0:
                    dp[t] = min(dp[t], 1 + dp[t-c])




        if dp[amount] == amount +1:
            return -1
        return dp[amount]