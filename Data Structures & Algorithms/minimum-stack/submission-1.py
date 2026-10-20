class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #if empty
        if not self.minStack:
            self.minStack.append(val)
        #if non empty
        else:
            #if val is less than current min
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
