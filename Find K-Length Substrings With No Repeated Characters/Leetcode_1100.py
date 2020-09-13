class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        ans, i = 0, 0
        chars = set()
        for j in range(len(S)):
            while S[j] in chars:
                chars.remove(S[i])
                i += 1
            chars.add(S[j])
            ans += j - i + 1 >= K
        return ans

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        N = len(S)
        if len(S) < K: return 0
        
        ans = 0
        cnt = collections.Counter(S[:K])
        for i in range(N-K+1):
            _, freq = cnt.most_common()[0] 
            if freq == 1:
                ans += 1
            if i+K<N:
                cnt[S[i]] -= 1
                cnt[S[i+K]] += 1
       
        return ans

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
