class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isalnum():
                stack.append(int(t))
            elif t == "+":
                stack.append(stack.pop() + stack.pop())

            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
                
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a//b)


        return stack[-1]
