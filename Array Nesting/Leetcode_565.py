# dfs => time complexity O(V+E) = O(N^2) where N=len(nums) 
# iterative version is much faster than recursive
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited, ans = set(), 0
        for num in nums:
            cnt, num2 = 0, num
            while num2 not in visited:
                visited.add(num2)
                cnt+=1
                num2 = nums[num2]
            ans = max(ans, cnt)
        return ans

# TLE
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
        
#         self.max_len = 0
        
#         def dfs(num: int, seen = set()):
#             self.max_len = max(self.max_len, len(seen))
#             if num in seen: 
#                 return
#             seen.add(num)
#             dfs(nums[num], seen)
#             seen.remove(num)
        
#         for num in nums:
#             dfs(num)
            
#         return self.max_len