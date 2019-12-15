# O(N) time solution
# but O(N) extra space
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        left_max, right_min = [arr[0]]*N, [arr[-1]]*N
        for i in range(1, N):
            left_max[i] = max(arr[i], left_max[i-1])
        for i in range(N-2, -1, -1):
            right_min[i] = min(arr[i], right_min[i+1])
        return 1 + sum(left_max[i] <= right_min[i+1] for i in range(N-1))
  
# AC but slow
# O(NlgN) time complexity for worst case input
# O(N) extra space in worst case but much better than that amortized
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr2 = sorted(arr)
        res = 0
        start = 0
        for i, a in enumerate(arr):
            if start == i and a == arr2[i]: 
                res+=1
            elif sorted(arr[start:i+1]) == arr2[start:i+1]:
                res += 1
                start = i+1
        return res
