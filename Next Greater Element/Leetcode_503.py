class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1]*len(nums)
        for idx in range(len(nums)):
            while stack and (nums[idx] > nums[stack[-1]]):
                res[stack.pop()] = nums[idx]
            stack += [idx]
        return res
