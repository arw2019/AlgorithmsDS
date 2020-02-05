# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.ans = 0
    
        def dfs(node):
            if node:
                subtree_min, subtree_max = node.val, node.val
                if node.left:
                    subtree_min = min(node.val, dfs(node.left)[0])   
                    self.ans = max(self.ans, node.val - subtree_min)
                if node.right:
                    subtree_max = max(node.val, dfs(node.right)[1])
                    self.ans = max(self.ans, subtree_max - node.val)
                # print(f'node={node.val}, subtree_min={subtree_min}, subtree_max={subtree_max}')    
                return subtree_min, subtree_max
                
        dfs(root)
        
        return self.ans
