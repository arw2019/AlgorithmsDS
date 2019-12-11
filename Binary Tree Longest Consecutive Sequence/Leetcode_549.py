# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node: TreeNode, parent: TreeNode) -> '[int, int]':
            if not node: return 0,0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            self.res = max(self.res, li+rd+1, ld+ri+1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        dfs(root, root)
        return self.res
