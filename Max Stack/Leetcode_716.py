# solution using stack + heap + boolean flag DS
# top 0.5%
from heapq import heappush, heappop

class Node:
    def __init__(self, v: int):
        self.v = v
        self.removed = False
    def __repr__(self):
        return "{v} ({removed})".format(v=self.v, removed=self.removed)
    
class MaxStack:
    
    def __init__(self):
        self.stack  = []
        self.heap = []
        self.i = 0
        
    def push(self, x: int) -> None:
        self.i += 1
        node = Node(x)
        self.stack.append(node)
        heappush(self.heap, (-x, -self.i, node))
        
    def pop(self) -> int:
        while True:
            node = self.stack.pop()
            if node.removed:
                continue
            node.removed = True
            return node.v
        
    def top(self) -> int:
        while True:
            if self.stack[-1].removed:
                self.stack.pop()
                continue
            return self.stack[-1].v
        
    def peekMax(self) -> int:
        while True:
            if self.heap[0][2].removed:
                heappop(self.heap)
                continue
            return self.heap[0][2].v
        
    def popMax(self) -> int:
        while True:
            _, _, node = heappop(self.heap)
            if node.removed:
                continue
            node.removed = True
            return node.v
        
# 1st attempt: top 36%
# class MaxStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack  = []
        

#     def push(self, x: int) -> None:
#         if self.stack: self.stack.append((x, max(x, self.peekMax())))
#         else: self.stack.append((x, x))

#     def pop(self) -> int:
#         return self.stack.pop()[0]

#     def top(self) -> int:
#         return self.stack[-1][0]

#     def peekMax(self) -> int:
#         return self.stack[-1][1] if self.stack else None

#     def popMax(self) -> int:
#         if not self.stack: return None
#         stack2 = []
#         curMax = self.peekMax()
#         while self.stack[-1][1] == curMax:
#             x = self.stack.pop()
#             if x[0] < curMax: stack2.append(x)
#             else: break
#         while stack2:
#             self.push(stack2.pop()[0])
#         return curMax

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
