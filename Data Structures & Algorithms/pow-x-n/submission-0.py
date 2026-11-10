class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            res = 1
            for i in range(n):
                res *= x

            return res

        denom = 1
        for i in range(-n):
            denom *=x
        return 1/denom