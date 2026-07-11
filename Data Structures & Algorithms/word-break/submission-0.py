class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0]  =True

        for i in range(1,len(s)+1):
            for w in wordDict:
                if i >= len(w) and w == s[i-len(w):i]:
                    if dp[i-len(w)]:
                        dp[i] = True
                        break
        
        return dp[len(s)]
