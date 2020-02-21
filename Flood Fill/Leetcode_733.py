class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not (image and image[0]): return [[]] 
        
        m, n = len(image), len(image[0])
        
        oldColor = image[sr][sc]
        
        seen = set()
        
        def dfs(pr: 'pixel row', pc: 'pixel column', seen):
            if (pr, pc) in seen or not (0<=pr<m and 0<=pc<n): 
                return
            if image[pr][pc] == oldColor:
                seen.add((pr, pc))
                dfs(pr+1, pc, seen)
                dfs(pr-1, pc, seen)
                dfs(pr, pc+1, seen)
                dfs(pr, pc-1, seen)
       
        dfs(sr, sc, seen) 
    
        for i, j in seen:
            image[i][j] = newColor
            
        return image
