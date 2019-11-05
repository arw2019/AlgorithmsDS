class Solution:
    def maxNumberOfApples(self, arr: List[int], maximum: int = 5000) -> int:
        arr.sort()
        tot, i = 0, 0
        while i<len(arr):
            newtot = tot + arr[i]
            if newtot < maximum: 
                tot = newtot
                i+=1
            else:
                break
        return i
