# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.modes, self.maxFreq = set(), 0
        self.curVal, self.no_occurences = None, 0
        def inorder(node):
            
            if not node: return
            
            inorder(node.left)
            
            if node.val != self.curVal:
                self.curVal = node.val
                self.no_occurences = 1
            else:
                self.no_occurences += 1
                
            if self.no_occurences == self.maxFreq:
                self.modes.add(self.curVal)
            elif self.no_occurences > self.maxFreq:
                self.maxFreq = self.no_occurences
                self.modes.clear()
                self.modes.add(self.curVal)
                
            inorder(node.right)
            
        inorder(root)
        
        return list(self.modes)
            
