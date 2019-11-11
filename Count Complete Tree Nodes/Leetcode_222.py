# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# AC solution using DFS
# top 30%
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        #to obtain height of tree go down leftmost branch
        self.h = 0
        node = root
        while node:
            node = node.left
            self.h += 1
        self.missing = 0
        def dfs(node: TreeNode, depth: int):
            if node: 
                dfs(node.left, depth+1)            
                dfs(node.right, depth+1)
            elif depth < self.h: 
                self.missing += 1
        dfs(root, 0)
        return 2**self.h - 1 - self.missing