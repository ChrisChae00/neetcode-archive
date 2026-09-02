class MinStack:

    def __init__(self):
        self.stack = []
        self.minNumber = []

    def push(self, val: int) -> None:
        if not self.minNumber or val <= self.minNumber[-1]:
            self.minNumber.append(val)
        else: 
            self.minNumber.append(self.minNumber[-1])
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minNumber.pop()

        

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return 0 if not self.stack else int(self.minNumber[-1])