# same solution
# replaced pop operations on preorder with pointer

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndicies = {val:idx for idx, val in enumerate(inorder)}
        inorderLoc = 0 
        def helper(lo, hi):
            if lo>hi: return None
            nonlocal inorderLoc 
            root = TreeNode(preorder[inorderLoc])
            inorderLoc+=1
            mid = inorderIndicies[root.val]
            root.left = helper(lo, mid-1)
            root.right = helper(mid+1, hi)
            return root
        return helper(0, len(inorder)-1)

# O(N) time, O(N) space
# Issue: consumes preorder array
# Issue: pop(0) operations are O(length of array)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndicies = {val:idx for idx, val in enumerate(inorder)}
        def helper(lo, hi):
            if lo>hi: return None
            root = TreeNode(preorder.pop(0))
            mid = inorderIndicies[root.val]
            root.left = helper(lo, mid-1)
            root.right = helper(mid+1, hi)
            return root
        return helper(0, len(inorder)-1)
