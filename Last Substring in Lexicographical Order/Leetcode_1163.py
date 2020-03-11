class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        maxSeen = ""
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] > maxSeen:
                    maxSeen = s[i:j]
        return maxSeen
