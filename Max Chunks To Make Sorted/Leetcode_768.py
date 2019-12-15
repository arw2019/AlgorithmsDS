# AC but slow
# O(NlgN) time complexity for worst case input
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
