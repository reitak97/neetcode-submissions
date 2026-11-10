class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]": "[", ")":"(", "}":"{" }

        for char in s:
            if stack and char in closeToOpen:
                if closeToOpen[char] == stack[-1]:
                    stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True
        return False

      
        