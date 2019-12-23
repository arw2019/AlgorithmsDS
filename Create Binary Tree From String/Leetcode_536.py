# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str, node: TreeNode = TreeNode(0)) -> TreeNode:
        if not s: return None
        root, _ = self.helper(s, 0)
        return root
    def helper(self, s: str, i: int) -> 'TreeNode, int':
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()):
            i+=1
        node = TreeNode(int(s[start:i]))
        if i < len(s) and s[i] == '(':
            i += 1
            node.left, i = self.helper(s, i)
            i+=1
        if i < len(s) and s[i] == '(':
            i += 1
            node.right, i = self.helper(s, i)
            i+=1
        return node, i
