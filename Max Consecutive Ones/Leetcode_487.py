# O(N) time, O(N) space
# same asymptotic complexity but runs much faster
from collections import deque
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros = [-1] + [i for i, num in enumerate(nums) if not num] + [len(nums)]
        return max([zeros[i+1] - zeros[i-1] - 1 for i in range(1, len(zeros)-1)]) if len(zeros) > 2 else len(nums)
    
# O(N) time, O(1) space
from collections import deque
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        for num in nums:
            r += 1
            if num == 0: 
                l, r = r, 0
            ans = max(ans, l+r)
        return ans