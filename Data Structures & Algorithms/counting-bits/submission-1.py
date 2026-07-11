class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            
            add = 0
            while i !=0:
                add += i%2
                i = i//2
            res.append(add)

        return res
