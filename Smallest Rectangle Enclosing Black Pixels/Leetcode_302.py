class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        if not (image and image[0]): return 0
        
        M, N = len(image), len(image[0])
        hMin, vMin, hMax, vMax = M-1, N-1, 0, 0
        
        seen = set()
        def dfs(i: int, j: int, seen: set) -> None:
            nonlocal hMin, vMin, hMax, vMax
            if 0<=i<M and 0<=j<N and image[i][j]=='1' and (i, j) not in seen:
                # print(f'i={i}, j={j}') 
                hMin, hMax = min(hMin, i), max(hMax, i)
                vMin, vMax = min(vMin, j), max(vMax, j)
                seen.add((i,j))
                dfs(i+1, j, seen)
                dfs(i-1, j, seen)
                dfs(i, j+1, seen)
                dfs(i, j-1, seen)
        
        dfs(x, y, seen)
        
        # print(f'horizontal boundaries = ({hMax}, {hMin})')  
        # print(f'vertical boundaries = ({vMax}, {vMin})')  
        
        return (hMax-hMin+1)*(vMax-vMin+1)
