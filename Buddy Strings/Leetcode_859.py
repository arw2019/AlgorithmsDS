from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        indicies = [i for i in range(len(A)) if A[i] != B[i]]
        if len(indicies) == 0:
            return any(freq>1 for _, freq in Counter(A).items())
        elif len(indicies) == 2:
            i, j = indicies
            return (A[i] == B[j] and B[i] == A[j])
        return False
