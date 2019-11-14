class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # preprocess the array with sort 
        # in a sorted array minimum differences occur for adjacent elements
        arr.sort()
        n, minDiff = len(arr), float('inf')
        [minDiff:=min(minDiff, arr[i]-arr[i-1]) for i in range(1,n)]
        ans = [[arr[i-1], arr[i]]for i in range(1,n) if arr[i]-arr[i-1] == minDiff]
        return ans
