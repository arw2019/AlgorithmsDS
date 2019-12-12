class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indicies = [i for i, char in enumerate(S) if char == C]
        return [min([abs(i-idx) for idx in indicies]) for i, char in enumerate(S)]
