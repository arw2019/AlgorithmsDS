   class RLEIterator:

    def __init__(self, A: List[int]):
        self.dq = collections.deque()
        for i in range(0,len(A),2):
            if A[i]:
                self.dq.append(A[i:i+2])
        #print(self.dq)

    def next(self, n: int) -> int:
        while n and self.dq:
            cnt, num = self.dq.popleft()
            if cnt >= n: 
                cnt -= n
                if cnt: self.dq.appendleft([cnt, num])
                return num
            else:
                n -= cnt
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)