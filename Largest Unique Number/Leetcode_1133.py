# top 0.25%
# collections.Counter object is very efficient!
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        ans = -1
        for k,v in collections.Counter(A).items():
            if v == 1 and k > ans:
                ans = k
        return ans

# top 2%
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        singles, multiples = set(), set()
        maxNum = float('-inf')
        for a in A:
            if not (a in singles or a in multiples): 
                singles.add(a)
            elif a in singles:
                singles.remove(a)
                multiples.add(a)
        return max(singles) if singles else -1
