class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        mySet = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l+=1
            mySet.add(s[r])
            longest = max(longest,r-l+1)
        return longest