# slighly faster - cuts down search space & handles some edge cases by hand
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        if not A or len(A) < 3: return []
        A.sort()
        if A[0] == A[-1] == 0: return [[0,0,0]]
        if A[0] >= 0 or A[-1] <= 0: return []
        res = []
        non_zero_index = next(index for index, val in enumerate(A) if val > 0)
        for pivot in range(non_zero_index):
            # skip if already computed
            if pivot > 0 and A[pivot-1] == A[pivot]:
                continue
            left = pivot+1
            right = len(A)-1
            while left < right:
                tot = A[pivot] + A[left] + A[right]
                if tot > 0:
                    while left < right and A[right] == A[right-1]:
                        right -= 1
                    right -=1
                elif tot < 0:
                    while left < right and A[left] == A[left+1]:
                        left += 1
                    left += 1
                else:
                    res.append([A[pivot], A[left], A[right]])
                    while left < right and A[right] == A[right-1]:
                        right -= 1
                    while left < right and A[left] == A[left+1]:
                        left += 1
                    right -= 1
                    left += 1
        return res

#------------------------------------------------------------------
    
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        res = []
        for i in range(len(A)-2):
            if i == 0 or (i > 0 and A[i]!=A[i-1]):
                lo, hi, tot = i+1, len(A)-1, 0-A[i]
                while lo < hi:
                    if A[lo] + A[hi] == tot:
                        res += [[A[i], A[lo], A[hi]]]
                        while lo < hi and A[lo] == A[lo+1]: lo += 1
                        while lo < hi and A[hi-1] == A[hi]: hi -= 1
                        lo += 1
                        hi -= 1 
                    elif A[lo] + A[hi] < tot:
                        while lo < hi and A[lo] == A[lo+1]: lo += 1
                        lo += 1
                    else:
                        while lo < hi and A[hi-1] == A[hi]: hi -= 1
                        hi -= 1
        return res

#-----------------------------------
# hashtable solution
# O(N^2) runtime, O(N) space

from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        uniqueNums = list(sorted(cnt.keys()))
        res = []
        for i, a in enumerate(uniqueNums):
            for j, b in enumerate(uniqueNums[i:], i):
                c = - (a + b)
                if a == b == c:
                    if cnt[a] >= 3: res+=[[a,a,a]]
                elif a == b:
                    if cnt[a]>=2 and cnt[c] > 0: res += [[a, a, c]]
                elif c == a or c == b:
                    if cnt[c] >=2: res += [[a, b, c]]
                else:
                    if cnt[c] > 0: res += [[a, b, c]]
        return list(set(tuple(sorted(triplet)) for triplet in res))
