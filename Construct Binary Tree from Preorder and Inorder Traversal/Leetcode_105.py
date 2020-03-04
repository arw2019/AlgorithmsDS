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
