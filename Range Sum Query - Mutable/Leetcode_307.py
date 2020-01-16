# Segment Tree Solution
# inspired by this article: http://codeforces.com/blog/entry/18051

class NumArray:

    def __init__(self, nums: List[int]):
        self._len = len(nums)
        self._tree = [0] * self._len + nums
        for i in range(self._len-1, 0, -1):
            self._tree[i] = self._tree[i<<1] + self._tree[i<<1|1]

    def update(self, i: int, val: int) -> None:
        """
        Modifies the array by updating the element at index i to val.
        Time complexity: O(lg(N))
        """
        n = self._len + i
        self._tree[n] = val
        while n > 1:
            self._tree[n>>1] = self._tree[n]+ self._tree[n^1]
            n>>=1

    def sumRange(self, i: int, j: int) -> int:
        """
        Finds the sum of elements between indicies i and j (i<=j) inclusive.
        Time complexity: O(lg(N))
        """
        m, n = self._len+i, self._len+j
        ans = 0
        while m <= n:
            if m & 1:
                ans += self._tree[m]
                m += 1
            m >>= 1
            if not n&1:
                ans += self._tree[n]
                n-=1
            n >>= 1
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
