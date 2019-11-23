# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 1%
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if x is root or y is root: return False
        
        self.info = None
    
        def dfs(cur: TreeNode, parent: TreeNode, depth: int, target: int) -> None:
            if cur.val == target:
                self.info = [depth, parent]
            if cur.left: dfs(cur.left, cur, depth+1, target)
            if cur.right: dfs(cur.right, cur, depth+1, target)
        
        dfs(root, None, 0, x)
        x_depth, x_parent = self.info.copy()
        dfs(root, None, 0, y)
        y_depth, y_parent = self.info.copy()
                
        if x_depth == y_depth and x_parent != y_parent:
            return True
        return False
