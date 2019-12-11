# slow - bottom 12%
# O(N) time, O(k) space solution
from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0: return float('-inf')
        window = deque()
        ws, maxWS = 0, float('-inf') # current and maximum window sum
        for n in nums:
            if len(window) == k:
                ws -= window.popleft()
            window.append(n)
            ws += n
            if len(window) == k: maxWS = max(maxWS, ws)
        return maxWS/k
