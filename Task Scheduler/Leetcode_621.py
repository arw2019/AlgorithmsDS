# correct but slow

from collections import Counter
from heapq import heappush, heappop, merge
import itertools

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        debug = False
        
        pq, tot = [], 0
        
        timer = itertools.count()
        start = next(timer)
        
        for char, freq in Counter(tasks).items():
            heappush(pq, (-freq, start, char))
            
        cur = start
        for _ in range(n): cur = next(timer)
                
        while pq:
            cooldown = []
            
            while pq:
                neg_freq, time, char = heappop(pq)
                freq = -1 * neg_freq
                if cur - time < n:
                    heappush(cooldown, (-freq, time, char))
                else:
                    break
            else:
                if debug: print('Going idle.')
                tot += 1
                pq = cooldown
                cur = next(timer)
                continue
            
            pq = list(merge(pq, cooldown))
            
            tot += 1
            cur = next(timer)
            if freq > 1:
                heappush(pq, (-(freq-1), cur, char))
                if debug: print(f'Dropped to-do number of {char} to {freq}.')
            else: # freq == 1
                if debug: print(f'Exhausted {char}.')
    
                
                
        return tot
                
