class MinStack:

    def __init__(self):
        self.stack = []
        self.sortedStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.sortedStack or self.sortedStack[-1] > val:
            self.sortedStack.append(val)
        else: self.sortedStack.append(self.sortedStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.sortedStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.sortedStack[-1]

        
