# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, 
                        root: TreeNode, 
                        maxVal = 0,
                        minVal = 100_000
                       ) -> int:
        
        if not root: return maxVal - minVal
        
        left = self.maxAncestorDiff( \
                    root.left, \
                    max(maxVal, root.val), \
                    min(minVal, root.val) \
            )
        right = self.maxAncestorDiff( \
                    root.right, \
                    max(maxVal, root.val), \
                    min(minVal, root.val) \
            )
        
        return max(left, right)
        
