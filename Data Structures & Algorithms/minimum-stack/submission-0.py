class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[len(self.min_stack) - 1]))

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)
        self.min_stack.pop(len(self.min_stack) - 1)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
