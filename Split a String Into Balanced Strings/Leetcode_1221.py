from itertools import accumulate
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return sum(
            z.real == z.imag 
            for z in accumulate((
                1 if char == 'L' else 1 for char in s
            ))
        )
