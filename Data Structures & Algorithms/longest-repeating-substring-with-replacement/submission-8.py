class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #window - maxf > k
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] +=1
            maxf = max(maxf,count[s[r]])

            win = r-l +1
            if(win - maxf > k):
                count[s[l]] -=1
                l+=1

            if (win-maxf <=k):
                res = max(res,win)


        return res
