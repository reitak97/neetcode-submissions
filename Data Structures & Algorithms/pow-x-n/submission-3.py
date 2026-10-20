class Solution:
    def myPow(self, x: float, n: int) -> float:
        def res(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x 
            

            if n%2 == 0:
                return res(x*x,n//2)
            else:
                return x * res(x*x,n//2)






        if x == 0:
            return 0

        elif n > 0:
            return res(x,n)

        else:
            n = abs(n)
            return 1/(res(x,n))


    