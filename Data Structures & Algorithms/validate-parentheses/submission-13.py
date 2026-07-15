class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]": "[", ")":"(", "}":"{" }

        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
                
            else:
                stack.append(char)

        if not stack:
            return True
        return False

      
        