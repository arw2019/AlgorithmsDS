# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        self.cache = set()
        
        def generate_cache(node):
            if node:
                generate_cache(node.left)
                self.cache.add(target - node.val)
                generate_cache(node.right)
        
        generate_cache(root1)
        
        self.ans = False
        
        def check_if_present(node):
            if node:
                if not self.ans: check_if_present(node.left)
                self.ans = self.ans or (node.val in self.cache)
                if not self.ans: check_if_present(node.right)
        
        check_if_present(root2)
        
        return self.ans
