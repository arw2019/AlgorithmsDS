# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, S, T):
        return not (S or T) or (
            (S and T)
            and S.val == T.val
            and self.isSameTree(S.left, T.left)
            and self.isSameTree(S.right, T.right)
        )

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s is not None and (
            self.isSameTree(s, t)
            or self.isSubtree(s.left, t)
            or self.isSubtree(s.right, t)
        )
