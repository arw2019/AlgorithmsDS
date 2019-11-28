# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        levelOrder = [root]
        i = 0
        while levelOrder[i]:
            levelOrder.append(levelOrder[i].left)
            levelOrder.append(levelOrder[i].right)
            i += 1
        return not any(levelOrder[i:])
