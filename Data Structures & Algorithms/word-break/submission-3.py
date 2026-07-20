class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if word == s[i-len(word):i] and i - len(word) <= len(s):
                    if dp[i-len(word)]:
                        dp[i] = True
                        
               
                

        return dp[len(s)]