from itertools import accumulate
from bisect import bisect_left
from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.cumWeights = list(accumulate(w))
        self.size = self.cumWeights[-1]
        

    def pickIndex(self) -> int:
        r = randint(1, self.size)
        return bisect_left(self.cumWeights, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
