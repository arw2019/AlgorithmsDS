# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def are_keys_in_range(tree, 
                              lowRange=float('-inf'), 
                              highRange=float('inf')):
            if not tree: return True
            elif not lowRange<tree.val<highRange:
                return False
            return are_keys_in_range(tree.left, lowRange, tree.val) and \
                    are_keys_in_range(tree.right, tree.val, highRange)
        
        return are_keys_in_range(root)
