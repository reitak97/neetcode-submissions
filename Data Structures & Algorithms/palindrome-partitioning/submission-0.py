class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def validPalindrome(string):
            l = 0
            r = len(string) -1 
            while l < r:
                if string[l] != string[r]:
                    return False
                l +=1
                r-=1
            
            return True
        res = []
        part = []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                

                #continue if palin
                if validPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res
            

        #start new string

        #continue
        

       