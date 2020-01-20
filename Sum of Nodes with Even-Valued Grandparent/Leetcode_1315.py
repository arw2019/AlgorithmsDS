from collections import namedtuple

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        Ancestors = namedtuple('Ancestors','grandparent parent')
        self._sum = 0
        
        def dfs(node: TreeNode, ancestors: 'ancestors'):
            if not node: 
                return
            if ancestors.grandparent == True:
                self._sum += node.val
            ancestors = Ancestors(ancestors.parent, node.val % 2 == 0)
            dfs(node.left, ancestors)
            dfs(node.right, ancestors)
        
        if root:
            dfs(root, Ancestors(False, False))
        
        return self._sum
