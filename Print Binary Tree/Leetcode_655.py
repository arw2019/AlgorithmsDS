# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def height(node: TreeNode) -> int:
            return 1 + max(height(node.left), height(node.right)) if node else 0
        
        def dfs(node: TreeNode, depth: int, level: int, position: int) -> None:
            self.ans[level][position] = str(node.val)
            if node.left:
                dfs(node.left, depth, level+1, position - 2**(depth -level-2))
            if node.right:
                dfs(node.right, depth, level+1, position + 2**(depth -level-2))
                
        
        h = height(root)
        self.ans = [[''] *(2**h - 1) for _ in range(h)]
        dfs(root, h, 0, (2**h-1) >> 1)
        return self.ans
