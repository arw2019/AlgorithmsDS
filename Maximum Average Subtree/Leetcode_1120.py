# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxAvg = float('-inf')
    
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.helper(root)
        return self.maxAvg
        
    def helper(self, root: TreeNode) -> 'int, int':
        if not root: return 0, 0

        tot, numNodes = root.val, 1
        totLeft, numLeft = self.helper(root.left)
        totRight, numRight = self.helper(root.right)
        tot += totLeft + totRight
        numNodes += numLeft + numRight
        
        self.maxAvg = max(self.maxAvg, tot/numNodes) 
        
        return tot, numNodes
