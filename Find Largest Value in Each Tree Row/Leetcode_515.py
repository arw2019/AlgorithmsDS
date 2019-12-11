# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        row = [root]
        res = []
        while row:
            newRow = []
            maxVal = float('-inf')
            for node in row:
                maxVal = max(maxVal, node.val)
                if node.left: newRow += [node.left]
                if node.right: newRow += [node.right]
            res += [maxVal]
            row = newRow
        return res
