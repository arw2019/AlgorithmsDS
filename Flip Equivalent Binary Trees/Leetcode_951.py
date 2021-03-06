# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 2%
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not (root1 or root2): return True
        if root1 and root2:
            if root1.val == root2.val:
                return (self.flipEquiv(root1.left, root2.left) \
                        and self.flipEquiv(root1.right, root2.right)) \
                    or (self.flipEquiv(root1.left, root2.right) \
                        and self.flipEquiv(root1.right, root2.left))
            else:
                return False
        return False
        
