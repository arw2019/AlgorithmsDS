# bottom-up state machine solution

from collections import namedtuple

class Solution:
    def checkRecord(self, n: int) -> int:
        
        debug = False
        
        mod = lambda x: x % (10**9 + 7)
        
        State = namedtuple('State', 'A0L0 A0L1 A0L2 A1L0 A1L1 A1L2')
        
        cur = State(1, 1, 0, 1, 0, 0)
        
        for _ in range(2, n+1):
            cur = State(
                mod(sum(cur[:3])),
                cur.A0L0,
                cur.A0L1,
                mod(sum(cur)),
                cur.A1L0,
                cur.A1L1
            )
            if debug: print(cur)
            
        return mod(sum(cur))


# top-down
# correct but excessive recursion depth for n > 40000

from functools import lru_cache
class Solution:
    def checkRecord(self, n: int) -> int:
        
        mod = 10**9 + 7
        
        @lru_cache(maxsize=None)
        def f(no_absences: bool, num_lates: '0, 1 or 2', num_chars: 'num chars processed') -> int:
            # print(f'Processed {num_chars} characters.')
            if num_chars == n-1:
                return 1 + no_absences + (num_lates < 2) * 1
            ans = 0
            if no_absences: ans += f(False, 0, num_chars + 1)
            if num_lates < 2:
                ans += f(no_absences, num_lates+1, num_chars + 1)
            ans += f(no_absences, 0, num_chars+1)
            return ans % mod
        
        return f(True, 0, 0)
