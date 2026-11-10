class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        def dfs(curr,length):

            if curr > amount:
                return 1e9
            
            if curr == amount:
                return length
            

            res = 1e9

            for c in coins:
                res = min(res,dfs(curr+c, length+1))

            return res

        minCoins = dfs(0,0)
        return -1 if minCoins >= 1e9 else minCoins
