class Solution:

    def subsetSum(self, nums: List[int], target: int): 
        """
        returns any combination of elements in nums that sums to target
        elements of nums may be used more than once
        elements of numbers are guaranteed to be positive
        """

        def helper(t, choice):
            """
            returns True if target possible else False
            choice carries a valid combination if one exists
            """        
            if t == 0:
                return True
            for n in nums:
                if n > t:
                    break
                else:
                    choice += [n]
                    if helper(t-n, choice):
                        return True
                    else:
                        choice.pop()
            return False
        
        ans = []
        helper(target, ans)

        if sum(ans) == target:
            return ans
        else:
            raise ValueError("No combination sums to target.")

s = Solution()
input1, target1 = [3, 6, 10, 12, 15, 20], 38
output1 = s.subsetSum(input1, target1)
assert sum(output1) == target1 
