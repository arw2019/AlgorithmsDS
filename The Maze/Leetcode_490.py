class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        m, n = len(maze), len(maze[0])
        
        self.found = False
        self.seen = set()

        def dfs(i, j):
            if (i,j) in self.seen or not (0<=i<m and 0<=j<n): 
                return
            else:
                
                if i == destination[0] and j == destination[1]:
                    self.found = True
                
                self.seen.add((i, j))
                
                if not self.found: 
                    I, J = i, j
                    while True:
                        if I < m-1 and maze[I+1][J] == 0:
                            I += 1
                        else:
                            break
                    if (I, J) != (i, j):
                        dfs(I, J)

                if not self.found: 
                    I, J = i, j
                    while True:
                        if I > 0 and maze[I-1][J] == 0:
                            I -= 1
                        else:
                            break
                    if (I, J) != (i, j):
                        dfs(I, J)
                
                if not self.found: 
                    I, J = i, j
                    while True:
                        if J > 0 and maze[I][J-1] == 0:
                            J -= 1
                        else:
                            break
                    if (I, J) != (i, j):
                        dfs(I, J)
                
                if not self.found: 
                    I, J = i, j
                    while True:
                        if J < n-1 and maze[I][J+1] == 0:
                            J += 1
                        else:
                            break
                    if (I, J) != (i, j):
                        dfs(I, J)
                                
    
        dfs(*start)
        
        return self.found
