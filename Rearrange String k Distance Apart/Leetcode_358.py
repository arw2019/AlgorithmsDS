# a more efficient solution 
# build up result from buckets
# don't have to compute result if invalid

from collections import Counter

class Solution:
    def rearrangeString(self, S: str, k: int) -> str:
        if k <= 1: return S
        cnt = Counter(S)
        M = max(cnt.values())
        nM = list(cnt.values()).count(M)
        if (M-1)* k + nM > len(S):
            return ''
        mostCommon = [char for char, _ in cnt.most_common(nM)]
        bucket = [''.join(mostCommon)] * M
        cnt -= Counter(mostCommon * M)
        for idx, char in enumerate(cnt.elements()):
            bucket[idx%(M-1)] += char
        return ''.join(bucket)

# AC solution using a priority queue to build up the result

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
