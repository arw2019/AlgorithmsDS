# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 0.3%
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        def dfs(node: TreeNode):
            if not node: return None
            if L <= node.val <= R:
                node.left, node.right = dfs(node.left), dfs(node.right)
                return node
            elif node.val < L:
                return dfs(node.right)
            else: # node.val > R
                return dfs(node.left)
        
        return dfs(root)
