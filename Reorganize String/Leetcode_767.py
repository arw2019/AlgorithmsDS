# greedy solution using priority queue

from heapq import heappop, heappush
class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = [0 for _ in range(26)]
        for c in S:
            counts[ord(c) - ord('a')] += 1
        heap = [] 
        for charNum, count in enumerate(counts):
            if count:
                heappush(heap, (-count, charNum))
        res = []
        prevCnt, prevCur = None, None 
        while heap:
            ncurCnt, curChar = heappop(heap)
            curCnt = -ncurCnt
            res.append(curChar)
            curCnt -= 1
            if prevCnt: 
                heappush(heap, (-prevCnt, prevChar))
            prevChar, prevCnt = curChar, curCnt
        if prevCnt:
            return ''
        else:
            return ''.join(map(lambda n: chr(n + ord('a')), res))
