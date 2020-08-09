class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[n+i//2] if i%2 else nums[i//2] for i in range(2*n)]

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [None]*(2*n)
        for i in range(2*n):
            if i%2: 
                res[i] = nums[n+i//2]
            else:
                res[i] = nums[i//2]
        return res

import itertools
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pairs = list(zip(nums[:n], nums[n:]))
        return list(itertools.chain(*pairs))

import itertools
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = nums[:n], nums[n:] 
        pairs = list(zip(x, y))
        return list(itertools.chain(*pairs))

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = nums[:n], nums[n:] 
        res = []
        for pair in zip(x, y):
            res += [*pair]
        return res
        
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = nums[:n], nums[n:] 
        res = []
        for i in range(n):
            res += [x[i], y[i]]
        return res
