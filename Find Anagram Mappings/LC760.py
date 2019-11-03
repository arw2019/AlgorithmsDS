import collections
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i, item in enumerate(B):
            d[item] += [i]
        ans = [None]*len(A)
        for i, item in enumerate(A):
            ans[i] = d[item].pop()
        return ans
