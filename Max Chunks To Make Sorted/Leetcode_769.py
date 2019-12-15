# linear time complexity
# O(N) space complexity for worst case input
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        vals, idxs = set(), set()
        for i, a in enumerate(arr):
            if not vals and a == i:
                res += 1
                continue
            else:
                vals.add(a)
                idxs.add(i)
            if vals == idxs:
                res += 1
                vals.clear()
                idxs.clear()
        return res
