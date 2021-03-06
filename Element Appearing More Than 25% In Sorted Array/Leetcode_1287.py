# O(lgN complexity solution)
import bisect
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n //4 == 0: return arr[0]
        for i in range(0, n, n//4):
            num = arr[i]
            if bisect.bisect_right(arr, num) - bisect.bisect_left(arr, num) > n//4:
                return num
 
# fast on LC testcases but O(N) solution
# from collections import Counter
# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         n = len(arr)
#         c = Counter(arr)
#         for num, freq in c.items():
#             if freq > n//4:
#                 return num
