# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            newLevel = []
            for node in queue:
                if node.left: newLevel.append(node.left)
                if node.right: newLevel.append(node.right)
            if not newLevel:
                return queue[0].val
            queue = newLevelL
