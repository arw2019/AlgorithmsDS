class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        idea from https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
        """
        
        self.debug = False
        
        if not nums: return []
    
        n = len(nums)
        
        self.smaller = [0] * n
        
        def helper(indicies: 'List[int]') -> 'List[int]':
            """
            merge sort + track left-to-right swaps
            """ 
            if self.debug: print(f'call to indicies... indicies= {indicies}') 
            N = len(indicies)
            mid = N // 2
            if mid:
                left, right = helper(indicies[:mid]), helper(indicies[mid:])
                if self.debug: print(f'left:{left}, right:{right}') 
                for i in reversed(range(N)):
                    if (not right) or (left and nums[left[-1]] > nums[right[-1]]):
                        self.smaller[left[-1]] += len(right)
                        indicies[i] = left.pop()
                    else:
                        indicies[i] = right.pop()
                    if self.debug: print(f"updated smaller: {self.smaller}")
            return indicies
        
        helper(list(range(n)))
        
        return self.smaller
        
