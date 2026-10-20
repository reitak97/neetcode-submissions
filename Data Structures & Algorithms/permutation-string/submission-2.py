class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s2Freq = {}

        for s in s1:
            s1Freq[s] = 1 + s1Freq.get(s,0)


        l = 0
        for r in range(len(s2)):
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r],0)


            #if frequency maps dont equal continue
            if s1Freq == s2Freq:
                return True

            #if length of window > lenght of s1, shift left pointer by 1
            if (r-l+1) > len(s1):
                if s2Freq[s2[l]] > 1:
                    s2Freq[s2[l]] -=1
                else:
                    del s2Freq[s2[l]]
                   
                if s1Freq == s2Freq:
                    return True
                l+=1

        return False

