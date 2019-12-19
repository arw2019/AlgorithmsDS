class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import collections
        d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        for num in nums:
            print(num)
            if target - num == num and len(d[num])>=2: 
                return d[num][:2]
            elif target - num != num and d[target-num]:
                return [d[num][-1], d[target-num][-1]]
