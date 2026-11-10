class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            #if close and stack not empty
            if stack and char not in openToClose:
                if char != openToClose[stack[-1]]:
                    return False
                stack.pop()

            #if open, push to stack
            elif char in openToClose:
                stack.append(char)

        if stack:
            return False
        else:
            return True
        
            
        




