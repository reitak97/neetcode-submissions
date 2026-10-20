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
        s = str(n)
        for char in s:
            res += int(char) ** 2

        return res

    