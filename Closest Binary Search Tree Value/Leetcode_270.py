# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#top 0.5%
# O(lg(N)) space
# class Solution:
#     def closestValue(self, root: TreeNode, target: float) -> int:
        
#         path = []
#         while root:
#             path += [root.val]
#             root = root.left if root.val > target else root.right
        
#         return min(path, key = lambda x: abs(target - x))
    
# slightly slower - top 2% - but O(1) space 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min((closest, root.val), key = lambda x: abs(x-target))
            root = root.left if root.val > target else root.right
        return closest
