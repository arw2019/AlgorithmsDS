# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
# O(h) time, O(h) space for function stack
# top 1% on LC
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

# iterative solution
# O(h) time, O(1) extra space
# top 50% on LC: constants must be better for recursive solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        while p.val>root.val or q.val<root.val:
            while p.val>root.val: root = root.right
            while q.val<root.val: root = root.left
        return root
