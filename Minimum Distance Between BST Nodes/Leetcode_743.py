# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev, self.ans = None, float('inf')
        
        def inorder(node: TreeNode):
            if not node: return
            inorder(node.left)
            if self.prev: 
                self.ans = min(self.ans, (node.val - self.prev))
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.ansMinimum Distance Between BST Nodes
