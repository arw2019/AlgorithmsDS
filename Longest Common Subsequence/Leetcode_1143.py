# top-down DP
# O(N^2) time, O(N^2) space

from functools import lru_cache
class Solution:
    @lru_cache()
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if min(len(text1), len(text2))<=0: return 0
        if text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        else:
            return max(self.longestCommonSubsequence(text1[:-1], text2), \
                      self.longestCommonSubsequence(text1, text2[:-1]))
