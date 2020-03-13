class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        states = set()
        for i in range(1, len(s)):
            if s[i-1:i+1] == '++':
                states.add(s[:i-1]+'--'+s[i+1:])
        return list(states)
