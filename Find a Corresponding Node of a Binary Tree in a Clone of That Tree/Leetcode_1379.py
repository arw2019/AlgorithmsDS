# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.ans = None
        
        def dfs(node: TreeNode) -> None:
            if not node: return
            if node.val == target.val:
                self.ans = node
            if self.ans is None: dfs(node.left)
            if self.ans is None: dfs(node.right)
    
        dfs(cloned)
        
        return self.ans
