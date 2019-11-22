# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 0.25%
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        level = maxLevel = 0
        largestTot = root.val
        while queue:
            level += 1
            newLevel, tot = [], 0
            for node in queue:
                tot += node.val
                if node.left: newLevel += [node.left]
                if node.right: newLevel += [node.right]
            if tot > largestTot:
                largestTot, maxLevel = tot, level
            queue = newLevel
        return maxLevel
