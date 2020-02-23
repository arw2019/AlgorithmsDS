class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(l) for l in zip(*A)]
