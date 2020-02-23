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

# O(n^2) solution for a square matrix

class Solution:
    
    def spiralOrder(self, square_matrix: List[List[int]]) -> List[int]:
        
        spiral_ordering: List[int] = []
        
        def matrix_layer_in_clockwise(offset):
            if offset == len(square_matrix) - offset - 1:
                spiral_ordering.append(square_matrix[offset][offset])
            else:
                spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
                spiral_ordering.extend(list(zip(*square_matrix))[-1-offset][offset:-1-offset])
                spiral_ordering.extend(square_matrix[-1-offset][-1-offset:offset:-1])
                spiral_ordering.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])
                
        for offset in range((len(square_matrix)+1)//2):
            matrix_layer_in_clockwise(offset)
        
        return spiral_ordering
