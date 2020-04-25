class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        P = list(range(1,m+1))
        for q in queries:
            idx= P.index(q)
            res += [idx]
            P = [q] + P[:idx] + P[idx+1:]
        return res
