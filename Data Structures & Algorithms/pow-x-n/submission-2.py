class Solution:
    def myPow(self, x: float, n: int) -> float:
        def res(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x 
            ress = res(x,n//2)

            if n%2 == 0:
                return ress * ress
            else:
                return x * ress * ress






        if x == 0:
            return 0

        elif n > 0:
            return res(x,n)

        else:
            n = abs(n)
            return 1/(res(x,n))


    