class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None for _ in range(maxSize)]
        self.maxSize = maxSize
        self.n = 0

    def push(self, x: int) -> None:
        if self.n < self.maxSize - 1:
            self.stack[self.n] = x
            self.n += 1
        print(self.stack)

    def pop(self) -> int:
        if self.n > 0:
            value = self.stack[self.n-1]
            self.stack[self.n] = None
            self.n -= 1
        else:
            value = -1
        return value

    def increment(self, k: int, val: int) -> None:
        i=0
        while i < k and i < self.n:
            self.stack[i] += val
            i += 1
        print(self.stack)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
