class Solution:
    def isHappy(self, n: int) -> bool:


        seen = set()
        curr = n
        while curr != 1:
            curr = self.sumOfSquares(curr)
            if curr in seen:
                return False
            seen.add(curr)

        return True

        


    def sumOfSquares(self,n):

        res = 0
        while n:
            digit = n % 10
            digit = digit **2
            res += digit
            n = n//10
        return res