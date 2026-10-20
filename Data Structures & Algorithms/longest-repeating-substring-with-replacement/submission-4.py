class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charCounter = {}
        l = 0
        maxF = 0
        for r in range(len(s)):

            charCounter[s[r]] = 1 + charCounter.get(s[r],0)
            maxF = max(maxF, charCounter[s[r]])
            while ((r-l+1-maxF > k)):
                charCounter[s[l]] -=1
                l +=1

            res = max(res, (r-l+1))

        return res




