from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt = Counter(T)
        ans = ""
        for char in S:
            ans += cnt[char] * char
            cnt[char] = 0
        for char, freq in cnt.items():
            if freq > 0:
                ans += cnt[char] * char
                cnt[char] = 0
        return ans
