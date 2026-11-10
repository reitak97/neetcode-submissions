class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):

            
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            #decode one way
            res = dfs(i+1)


            if i < len(s)-1:
                if (s[i] == '1' or
                (s[i] == '2' and s[i+1] < '7')):
                    res += dfs(i+2)

            return res
            dp[i] = res

        return dfs(0)