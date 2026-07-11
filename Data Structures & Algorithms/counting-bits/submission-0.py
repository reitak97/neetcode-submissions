class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            n = i
            add = 0
            while n !=0:
                add += n%2
                n = n//2
            res.append(add)

        return res
