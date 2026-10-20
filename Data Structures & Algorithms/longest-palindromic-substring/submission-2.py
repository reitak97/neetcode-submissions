class Solution:
    def longestPalindrome(self, s: str) -> str:
        #treat i as center and expand outwards

        #consider odd and even cases
        res = ""
        resLen = 0
        for i in range(len(s)):
            #for odd case start r and l to i
            r = l = i

            #while in obunds and equal
            while l >=0 and r < len(s) and s[l] == s[r]:
                #if longer than current palindrome
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = (r-l+1)
                l -=1
                r +=1

            
            #for even case set l = i and r = i +1
            l = i 
            r = i + 1
            while l >=0  and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = (r-l+1)

                l -=1
                r +=1
            
        return res
