import itertools
from heapq import heappop, heappush

class Solution:
    def rearrangeString(self, S: str, k: int) -> str:
        
        clock = itertools.count()
        
        occurences = [0 for _ in range(26)]
        for c in S:
            occurences[ord(c) - ord('a')] += 1
            
        active, cold = [], []
        for ordNum, cnt in enumerate(occurences):
            if cnt:
                heappush(active, (-cnt, float('-inf'), ordNum))
            
        res = []
        
        while active:
            curTime = next(clock)
            negativeCnt, lastUse, ordNum = heappop(active)
            cnt = -negativeCnt
            res.append(ordNum)
            cnt -= 1
            if cnt:
                cold.append((-cnt, curTime, ordNum))
            if cold and curTime - cold[0][1] >= k-1:
                heappush(active, heappop(cold))
        
        if cold:
            return '' 
        else:
            return ''.join(map(lambda n: chr(n + ord('a')), res))
