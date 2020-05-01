# an implementation of n-largest using heapq's basic methods
# time complexity: O(NlgN), space complexity: O(N)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -n)
        for _ in range(k-1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)
    
# solution using heapq library's built-in function
# equivalent to sorted(nums)[:n] 
# time complexity: O(NlgN), space complexity: O(N)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = heapq.nlargest(k, nums)
        return k_largest[-1]
