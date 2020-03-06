# Newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        y = x
        while y*y > x:
            y = (y + x//y) // 2
        return int(y)

# binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo+hi)//2
            guess = mid*mid
            if guess <= x:
                lo = mid+1
            else:
                hi=mid-1
        return lo-1
