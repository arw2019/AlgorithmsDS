# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ''
        if not (t.left or t.right): return str(t.val)
        if t.right and t.left: return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        if t.left: return str(t.val) + '(' + self.tree2str(t.left) + ')' 
        if t.right: return  str(t.val) + '()(' + self.tree2str(t.right) + ')'
