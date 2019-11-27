# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height = 0
        def dfs(node: TreeNode, h: int) -> int:
            if not node: return 0
            l, r = dfs(node.left, h+1), dfs(node.right, h+1)
            self.height = max(self.height, l+r)
            return 1 + max(l, r)
        dfs(root, 0)
        return self.height
