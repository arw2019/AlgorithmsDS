#top 3%
from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        self.aux = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack:
            return ValueError("The queue is empty.")
        while len(self.stack)>1:
            self.aux.append(self.stack.pop())
        x = self.stack.pop()
        while self.aux:
             self.stack.append(self.aux.pop())
        return x


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack:
            return ValueError("The queue is empty.")
        while len(self.stack)>1:
            self.aux.append(self.stack.pop())
        x = self.stack.pop()
        self.stack.append(x)
        while self.aux:
             self.stack.append(self.aux.pop())
        return x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
