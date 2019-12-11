# O(1) space but slower
# O(N) time
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n, c = len(nums), Counter(nums)
        for num in nums:
            c[num] += 1
            if len(c) == 3: 
                c -= Counter(set(c))
        return [num for num, freq in c.items() if nums.count(num)> n//3]
    
# O(N) time
# O(N) space but fast
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n, c = len(nums), Counter(nums)
        for num, freq in c.items():
            if freq > n//3: res.append(num)
        return res
