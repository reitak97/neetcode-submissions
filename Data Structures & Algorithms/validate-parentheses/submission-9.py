class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}": "{", ")": "("}
        stack = []

        for c in s:
            #check if closing char
            if c in closeToOpen:
                if stack and closeToOpen[c] != stack[-1]:
                    return False
                stack.pop()
                
            #if opening char, add to stack
            else:   
                stack.append(c)


            
        

        if not stack:
            return True
        return False

