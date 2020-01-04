class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ppl = [i for i, seat in enumerate(seats) if seat]
        res = max(ppl[i] - ppl[i-1] for i in range(1,len(ppl)))//2 if len(ppl) > 1 else 0
        if not seats[0]: res = max(res, ppl[0])
        if not seats[-1]: res = max(res, len(seats) - 1 - ppl[-1])
        return res
