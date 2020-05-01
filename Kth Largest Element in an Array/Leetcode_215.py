import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = heapq.nlargest(k, nums)
        return k_largest[-1]
