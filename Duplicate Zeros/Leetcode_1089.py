# 15 times faster!
# same time complexity but I relegate copy operations to python list.insert() method
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                arr.insert(idx+1, 0)
                arr.pop()
                idx += 2
            else:
                idx +=1
                
# correct solution but woefully slow (1760 ms)
# O(N^2) copy operations in nested while loops
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                j = len(arr)-1
                while j >= idx+1:
                    arr[j] = arr[j-1]
                    j -= 1
                idx +=2
            else:
                idx += 1