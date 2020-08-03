from itertools import chain
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(chain(*list(chain([(nums[i], nums[n+i]) for i in range(n)]))))
