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
