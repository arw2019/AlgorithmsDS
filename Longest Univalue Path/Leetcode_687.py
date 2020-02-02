# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        self.ans = 0
       
        def dfs(node: TreeNode):
            lPath, rPath = 0, 0 
            if node.left:
                if node.val == node.left.val:
                     lPath = 1 + dfs(node.left)
                else:
                    dfs(node.left)
            if node.right:
                if node.val == node.right.val:
                    rPath = 1 + dfs(node.right)
                else:
                    dfs(node.right)
            # print(f'node={node.val}, left:{lPath}, right: {rPath}')
            self.ans = max(self.ans, lPath+rPath)
            return max(lPath, rPath)            

        if root: dfs(root) 
        
        return self.ans
