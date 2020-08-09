# O(N) time, N=len(S)
# O(L) space, L = length of alphabet
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        for i, char in enumerate(S):
            d[char] = i
        ans = []
        start = 0
        cur, finished = set(), set()
        for i, char in enumerate(S):
            if d[char] == i: 
                finished.add(char)
            cur.add(char)
            if cur == finished:
                ans += [i+1-start]
                start = i+1
        return ans
