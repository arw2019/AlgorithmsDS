# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        ans = 0
        while queue:
            newLevel = []
            for node in queue:
                if node.left: 
                    if not (node.left.left or node.left.right):
                        ans += node.left.val
                    else: newLevel.append(node.left)
                if node.right: newLevel.append(node.right)
            queue = newLevel
        return ans
