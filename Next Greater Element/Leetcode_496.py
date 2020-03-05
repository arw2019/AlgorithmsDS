class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, d = [], {}
        i = 0
        for n in nums2:
            while stack and stack[-1] < n:
                d[stack.pop()] = n
            stack += [n]
        return [d.get(n,-1) for n in nums1]
