class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}": "{", ")": "("}
        stack = []
        for char in s:
            #if char is closing
            if char in closeToOpen:
                # "]"
                #check non empty stack and current matches most recent
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                #early return
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
