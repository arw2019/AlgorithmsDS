from heapq import heappush, heappop
class Solution:
    def pourWater(self, hts: List[int], V: int, K: int) -> List[int]:
        
        n, lHeap, rHeap = len(hts), [], []
        
        def moveLeft(l: int) -> int:
            while l>0 and hts[l] >= hts[l-1]:
                l -= 1
                heappush(lHeap, (hts[l], -l))
            return l
        
        def moveRight(r: int) -> int:
            while r<n-1 and hts[r] >= hts[r+1]:
                r += 1
                heappush(rHeap, (hts[r], r))
            return r
        
        left, right = moveLeft(K), moveRight(K)
    
        for _ in range(V):
            if lHeap and lHeap[0][0] < hts[K]:
                h, i = heappop(lHeap)
                i = -i
                hts[i] += 1
                heappush(lHeap, (hts[i], -i))
                if i == left: left = moveLeft(left)
            elif rHeap and rHeap[0][0] < hts[K]:
                h, i = heappop(rHeap)
                hts[i] += 1
                heappush(rHeap, (hts[i], i))
                if i == right: right = moveRight(right)
            else:
                hts[K] += 1
                if left == K: 
                    left = moveLeft(left)
                if right == K: 
                    right = moveRight(right)
        
        return hts
