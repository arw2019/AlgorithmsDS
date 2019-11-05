# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cnt = 0
    def bstFromPreorder(self, preorder: List[int], limit=float('inf')) -> TreeNode:
        if self.cnt == len(preorder) or preorder[self.cnt] > limit:
            return None
        root = TreeNode(preorder[self.cnt])
        self.cnt+=1
        root.left = self.bstFromPreorder(preorder, root.val) 
        root.right = self.bstFromPreorder(preorder, limit)
        return root
