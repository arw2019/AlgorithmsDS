# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: 
            p, q = q, p
            
        if p.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        while p.val>root.val or q.val<root.val:
            while p.val>root.val: root = root.right
            while q.val<root.val: root = root.left
        return root
