from collections import namedtuple

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        Status = namedtuple('Status','numTargets ancestor')
        
        def lca_helper(tree, p, q):
            if tree is None: return Status(0, None)
            l = lca_helper(tree.left, p, q)
            if l.numTargets==2: return l
            r = lca_helper(tree.right, p, q)
            if r.numTargets==2: return r
            numTargets = (l.numTargets + r.numTargets + (p,q).count(tree))
            return Status(numTargets, tree if numTargets==2 else None)
        
        return lca_helper(root, p, q).ancestor

# brute force solution
# O(n^2) runtime

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right
