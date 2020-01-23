# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        self.res = defaultdict(list)
      
        def dfs(node: 'TreeNode', 
                i: """horizontal location: 
                    0 for root, -ve left, +ve right"""
               ) -> None:
            if not node: return
            self.res[i].append(node.val)
            dfs(node.left, i-1)
            dfs(node.right, i+1)
            
        dfs(root, 0)
        
        ans = []
        for vertical_level in sorted(self.res.keys()):
            ans += [self.res[vertical_level]]
            
        return ans
