import itertools
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(itertools.chain  ([(nums[i], nums[n+i]) for i in range(n)]))
