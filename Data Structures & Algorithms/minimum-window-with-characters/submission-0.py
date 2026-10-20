class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res= ""
        tCount = {}
        resLen = len(s) + 1
        for char in t:
            tCount[char] = 1 + tCount.get(char,0)
        have = 0
        need = len(tCount)
        l = 0 

        window = {}
       
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tCount and window[c] == tCount[c]:
                have +=1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = s[l:r+1]

                window[s[l]] -=1
             
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -=1
                l +=1
        return res


