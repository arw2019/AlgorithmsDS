from heapq import heappush, heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for idx, l in enumerate(nums): heappush(heap, (l[0], idx, 0))
        interval = -1e9, 1e9
        largest = max(l[0] for l in nums)
        while heap:
            smallest, i, j = heappop(heap)
            if largest - smallest < interval[1] - interval[0]:
                interval = smallest, largest
            if j + 1 == len(nums[i]):
                return interval
            val = nums[i][j+1]
            largest = max(largest, val)
            heappush(heap, (val, i, j+1))
