# top 25%

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ht = collections.defaultdict(int)
        for i, n in enumerate(nums):
            ht[n] += 1
        nums = sorted(list(ht.keys()))
        N = len(nums)
        res = set()
        for i in range(N):
            n1 = nums[i]
            for j in range(i+1, N):
                n2 = nums[j]
                n3 = - (n1+n2)
                if (n3==n1 or n3==n2):
                    if ht[n3]>= 2: res.add(tuple(sorted([n1, n3, n2])))
                elif n3 in ht:
                     res.add(tuple(sorted([n1, n3, n2])))
        if 0 in ht and ht[0] >= 3:
            res.add((0, 0, 0))
        
        return res
