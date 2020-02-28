class Solution:
    def findMin(self, A: List[int]) -> int:
        left, right = 0, len(A)-1
        while left < right:
            mid = (left+right)//2
            if A[mid] > A[right]:
                left = mid+1
            else:
                right = mid
        return A[left]
