# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev, self.ans = float('inf'), float('inf')
        def inorder(node: TreeNode) -> None:
            if not node: return
            inorder(node.left)
            self.ans, self.prev = min(self.ans, abs(node.val - self.prev)), node.val
            inorder(node.right)
        inorder(root)
        return self.ans
