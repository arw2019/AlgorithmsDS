# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        level = [root]
        while level:
            newLevel = []
            tot, num = 0, 0
            for node in level:
                tot += node.val
                num += 1
                if node.left: newLevel.append(node.left)
                if node.right: newLevel.append(node.right)
            level = newLevel
            res.append(tot/num)
        return res
