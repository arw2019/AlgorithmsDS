# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def dfs(node: TreeNode) -> List[int]:
            if not (node.left or node.right):
                return [node.val]
            ans = []
            if node.left: ans += dfs(node.left) 
            if node.right: ans += dfs(node.right)
            return ans
        
        return dfs(root1) == dfs(root2)