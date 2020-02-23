# clean code and quick in practice
# but O(n^3) time complexity

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        
        while matrix:
            each run is O(n^2) and loop runs O(n) times
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1] 
        
        return ans
