class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # arithmetic series A + Ar + 2Ar + ...
        n = len(arr)
        A = arr[0]
        r = (arr[-1] - arr[0])//n
        if r == 0: return A
        val = A
        for a in arr:
            if a != val: return val
            val += r
