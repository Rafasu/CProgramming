class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minElement = 999999
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minElement = min(self.stack)
    
    def pop(self) -> None:
        if(len(self.stack) <= 1):
            self.stack.pop()
            return None
        self.stack.pop()
        self.minElement = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minElement
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()