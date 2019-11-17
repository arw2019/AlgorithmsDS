from collections import deque
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        K, res, cur, left = sum(data), 0, 0, -1
        for right, x in enumerate(data):
            cur += x
            if right - left > K:
                left += 1
                cur -= data[left]
            res = max(res, cur)
        return K - res