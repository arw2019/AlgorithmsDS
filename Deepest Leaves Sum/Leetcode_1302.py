# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root: return 
        
        self.height = 0
        self.sum_ = 0
        
        def dfs(node: TreeNode, h: int = 0) -> None:
            if not (node.left or node.right):
                if h == self.height:
                    self.sum_+= node.val
                elif h > self.height:
                    self.height = h
                    self._sum = node.val
            else:
                if node.left: dfs(node.left, h+1)
                if node.right: dfs(node.right, h+1)
        
        dfs(root)
        
        return self.sum_
    
*************************************************************************
# correct solution with two passes of dfs
    
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root: return 
        
        self.height = 0
        
        def dfs_1(node: TreeNode, h: int = 0) -> None:
            if not (node.left or node.right): 
                self.height = max(self.height, h)
            else:
                if node.left: dfs_1(node.left, h+1)
                if node.right: dfs_1(node.right, h+1)
        
        dfs_1(root)
        
        self._sum = 0
        
        def dfs_2(node: TreeNode, h: int = 0) -> None:
            if not node: return
            if h == self.height:
                self._sum += node.val
            dfs_2(node.left, h+1)
            dfs_2(node.right, h+1)
            
        dfs_2(root)
        
        return self._sum
