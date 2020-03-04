# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorderIndicies = {val:idx for idx, val in enumerate(inorder)}
        def helper(lo, hi):
            if lo > hi: return None
            root = TreeNode(postorder.pop())
            mid = inorderIndicies[root.val]
            root.right = helper(mid+1, hi)
            root.left=helper(lo, mid-1)
            return root
        return helper(0, len(inorder)-1)
