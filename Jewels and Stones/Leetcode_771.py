class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in set(J) for s in S)
