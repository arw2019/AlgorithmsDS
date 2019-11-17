# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node: TreeNode) -> bool:
            if node is None: return False
            if not dfs(node.left):
                node.left = None
            if not dfs(node.right):
                node.right = None
            if not (node.left or node.right):
                if node.val != 1:
                    node = None
                    return False
            return True
        
        dfs(root)
        
        return root
