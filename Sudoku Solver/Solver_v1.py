# I believe that this is a correct algorithm
# but very inefficient (I get TLE on Leetcode)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(i: int, j: int) -> bool:
            if i == 9:
                i=0
                j+=1
                if j == 9:
                    # entire board has been filled
                    return
                
            if board[i][j] != '.':
                return helper(i+1, j)
            
            def valid_to_add(i: int, j: int, num: int) -> bool:
                # check row constains
                if any(num == board[k][j] for k in range(9)): 
                    return False
                # check column constains
                if num in board[i]: 
                    return False
                # check subbox constraints
                I, J = i//3, j//3
                return not any([num == board[3*I+a][3*J+b] for a, b in itertools.product(range(3), repeat=2)])
            
            for num in range(9):
                if valid_to_add(i, j, num):
                    board[i][j] = num
                    if helper(i+1, j):
                        return True
                    # undo the assignment
                    board[i][j] = '.'
            return False
        
        helper(0,0)
        