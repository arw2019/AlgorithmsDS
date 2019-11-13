class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted(interval[0] for interval in intervals)
        ans = [-1] * len(intervals)
        d = {j[0]: i for i, j in enumerate(intervals)}
        k = 0
        for start, end in sorted(intervals, key= lambda x: x[1]):
            k = bisect.bisect_left(starts, end, k)
            if k < len(intervals): ans[d[start]] = d[starts[k]]
        return ans