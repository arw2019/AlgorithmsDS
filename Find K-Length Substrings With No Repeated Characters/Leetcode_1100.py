from collections import deque, defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        dq, d, repeats = deque(), defaultdict(int), set()
        ans = 0
        for s in S:
            if len(dq) == K:
                t = dq.popleft()
                if d[t] == 2: 
                    repeats.remove(t)
                d[t] -= 1
            dq.append(s)
            d[s] += 1
            if d[s] == 2:
                repeats.add(s)
            if len(dq) == K and len(repeats) == 0:
                ans+=1
        return ans