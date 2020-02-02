# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and node.left.val == target and not (node.left.left or node.left.right):
                node.left = None
            if node.right and node.right.val == target and not (node.right.left or node.right.right):
                node.right = None
            
        dfs(root)
        
        return root if (root.left or root.right or root.val != target) else None
