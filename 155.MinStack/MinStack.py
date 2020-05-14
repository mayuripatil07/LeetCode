class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.st = []

    def push(self, x: int) -> None:
        if len(self.stack) >=1:
            self.stack.append((x,min(x, self.stack[-1][1])))
        else:
            self.stack.append((x,x))



    def pop(self) -> None:
        if self.stack:
            a = self.stack[-1]
            self.stack.pop(-1)
        return a




    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return 0


    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
