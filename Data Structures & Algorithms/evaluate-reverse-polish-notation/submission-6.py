class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #divison truncates so int(a/b) to account for negative


        #use stack and call operand on top element

        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())

            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(t))


        return stack[-1]

      
        
