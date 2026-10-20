class Solution:
    def reverse(self, x: int) -> int:
        isPos = True
        if x < 0:
            isPos = False
        x = abs(x)
        res = 0
        while x:
            digit = x%10
            x = x//10
            res = res * 10 + digit
            if res > (2 ** 31 - 1):
                return 0
        if isPos:
            return res
        return res * -1


    
  
