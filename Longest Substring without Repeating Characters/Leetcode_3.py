# store current valid substring as str
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        cur, maxLen = "", 0
        for char in s:
            if char not in cur:
                cur += char
                maxLen = max(maxLen, len(cur))
            else:
                removed = cur.split(char)
                cur = removed[1] + char
        return maxLen
    
 # store current valid substring in a dict
 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1 if s else 0
        cur, start = {}, 0
        for i, char in enumerate(s):
            if char in cur:
                j = cur.pop(char)
                cur = {char2: k  for char2, k in cur.items() if k>j}
                start = min(cur.values()) if cur else i
            cur[char] = i
            res = max(res, i - start + 1)
        return res
