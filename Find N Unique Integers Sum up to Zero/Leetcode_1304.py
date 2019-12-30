from collections import deque
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = deque([0]) if n%2 else deque()
        for i in range(1, n, 2):
            res.append(i+(i+n)%2)
            res.appendleft(-i - (i+n)%2)
        return res
