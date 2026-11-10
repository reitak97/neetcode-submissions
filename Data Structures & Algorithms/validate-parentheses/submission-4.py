class Solution:
    def isValid(self, s: str) -> bool:
        pairM =  {"(" : ")", "{":"}", "[":"]"}


        stack = []
        for char in s:
            if char in pairM:
                stack.append(char)
            elif stack and char not in pairM:
                top = stack.pop()
                if pairM[top] != char:
                    return False
        
        return True


