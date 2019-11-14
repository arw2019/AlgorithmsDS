class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        
        def backtracking(pattern: str, s: str, d: dict):
            if not (pattern or s):
                return True
            if not pattern:
                return False
            for i in range(1, len(s) - len(pattern) + 2):
                if pattern[0] not in d and s[:i] not in d.values():
                    d[pattern[0]] = s[:i]
                    if backtracking(pattern[1:], s[i:], d):
                        return True
                    del d[pattern[0]]
                elif pattern[0] in d and d[pattern[0]] == s[:i]:
                    if backtracking(pattern[1:], s[i:], d):
                        return True
            return False
        
        return backtracking(pattern, string, {})