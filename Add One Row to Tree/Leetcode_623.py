# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot

        currentRow = [root]
        i = 1
        while  i < d-1:
            nextRow = []
            for node in currentRow:
                if node.left: nextRow.append(node.left)
                if node.right: nextRow.append(node.right)
            currentRow = nextRow
            i += 1 
        for node in currentRow:
            l, r = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left = l
            node.right.right = r
       
        return root
