# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        self.greaterSum = 0
        
        def dfs(node: TreeNode) -> None:
            """
            reverse inorder traversal of the tree
            """
            if not node: return
            dfs(node.right)
            self.greaterSum += node.val
            node.val = self.greaterSum
            dfs(node.left)
            
        dfs(root)
        
        return root
