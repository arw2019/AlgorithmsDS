# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.maxlen=1
        
    def dfs(self, root: TreeNode, cnt: int) -> None:
        self.maxlen = max(self.maxlen, cnt)
        if root.right:
            if root.right.val == root.val+1:
                self.dfs(root.right, cnt+1)
            else:
                self.dfs(root.right, 1)
        if root.left:
            if root.left.val == root.val+1:
                self.dfs(root.left, cnt+1)
            else:
                self.dfs(root.left, 1)
       
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0  #guarantees that we won't pass a Null argument to self.dfs
        self.dfs(root, 1)
        return self.maxlen
