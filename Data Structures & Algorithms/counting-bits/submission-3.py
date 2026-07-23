class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            add = 0
            while i:
                add += i%2
                i = i//2

            
            res.append(add)

        return res