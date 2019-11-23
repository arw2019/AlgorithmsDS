# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        
        self.cache = {}
        
        def dfs(node: TreeNode) -> None:
            if not node or node in self.cache: 
                return
            tot = 0
            if node.left:
                if node.left not in self.cache:
                    dfs(node.left)
                tot += self.cache[node.left]
            tot += node.val
            if node.right:
                if node.right not in self.cache:
                    dfs(node.right)
                tot += self.cache[node.right]
            self.cache[node] = tot
        
        dfs(root)
        
        sum_of_all = self.cache[root]
        
        for node, sum_subtree in self.cache.items():
            if node != root and 2 * sum_subtree == sum_of_all: 
                return True
        return False
