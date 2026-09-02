class MinStack:

    def __init__(self):
        self.stack = []
        self.minNumStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minNumStack or val <= self.minNumStack[-1]:
            self.minNumStack.append(val)
        else: 
            self.minNumStack.append(self.minNumStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minNumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNumStack[-1] 
