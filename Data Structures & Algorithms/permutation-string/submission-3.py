class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqs1 = defaultdict(int)
        for char in s1:
            freqs1[char] +=1


        freqs2 = defaultdict(int)
        #sliding window with fixed size equal to legnth of s1
        l = 0 
        for r in range(len(s2)):
            freqs2[s2[r]] +=1
            if freqs1 == freqs2:
                return True

            if(r-l+1) > len(s1):
                #either decrement
                if freqs2[s2[l]] > 1:
                    freqs2[s2[l]] -=1
                else:
                    del freqs2[s2[l]]

                if freqs1 == freqs2:
                    return True
                l +=1
        

        return False
