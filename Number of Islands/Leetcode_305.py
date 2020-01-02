class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        grid, parent = set(),  {}
        self.islands = 0
        
        def add(i: int, j: int) -> None:
            
            # location is outside the grid
            if not (0<=i<m and 0<=j<n) or (i, j) in grid: return
            
            grid.add((i,j))
            self.islands += 1
        
            neighbors = (i+1, j), (i-1, j), (i, j+1), (i, j-1)
            for k,l in neighbors:
                if (k,l) in grid: union(i, j, k, l)
        
        def find(i: int, j: int) -> int:
            if (i,j) not in parent: return i, j
            parent[i,j] = find(*parent[i,j])
            return parent[i,j]
        
        def union(i: int, j: int, k: int, l: int) -> None:
            # print(f'union: ({i},{j}) with ({k},{l})')
            p, q = find(i, j), find(k, l)
            p, q = min(p, q), max(p, q)
            if p!=q:
                # print('merge components')
                parent[q] = p 
                self.islands -=1
        
        ans = []
        for i, j in positions:
            add(i, j)
            # print(grid)
            ans.append(self.islands)
            
        return ans
