class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        cnt = 0
        contents = []
        for s in S:
            if s.islower():
                contents.append(s.upper())
            elif s.isdigit() or s.isupper():
                contents.append(s)
        ans = ''
        start = len(contents) % K
        if start: ans += ''.join(contents[:start]) + '-'
        for i in range(start, len(contents), K):
            ans += ''.join(contents[i:i+K])
            ans += '-'
        return ans[:-1]
