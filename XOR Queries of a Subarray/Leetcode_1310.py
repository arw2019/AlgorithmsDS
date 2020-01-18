class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefixVals = [arr[0]]
        for idx, a in enumerate(arr[1:], 1):
            prefixVals.append(prefixVals[idx-1] ^ a)
        
        ans = []
        
        for left, right in queries:
            if left == 0:
                ans.append(prefixVals[right])
            else:
                ans.append(prefixVals[left-1]^prefixVals[right])
            
        return ans
