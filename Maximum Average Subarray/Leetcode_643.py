# top 3% solution using iterators
# https://leetcode.com/problems/maximum-average-subarray-i/discuss/105435/2-lines-Python-2-versions
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0: return float('-inf')
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums))/k

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
