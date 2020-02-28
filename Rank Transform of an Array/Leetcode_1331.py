from bisect import bisect
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(list(set(arr)))
        for i, a in enumerate(arr):
            arr[i] = bisect(arr2, a)
        return arr
