class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(0,n+1):
            curr = 0 
            pos = i
            while i:
                curr += i%2
                i = i >> 1
            res[pos] = curr
        return res
            
                            
