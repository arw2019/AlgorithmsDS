# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
            
        # each node has unique val => use vals as vertex labels
        self.graph = defaultdict(list)
        self.leaves = set()
        
        def dfs(node: TreeNode):
            if not node: return
            if not (node.left or node.right):
                self.leaves.add(node.val)
            if node.left:
                self.graph[node.val] += [node.left.val]
                self.graph[node.left.val] += [node.val]
                dfs(node.left)
            if node.right:
                self.graph[node.val] += [node.right.val]
                self.graph[node.right.val] += [node.val]
                dfs(node.right)
        
        dfs(root)  
        
        queue, seen = [k], set()

        while queue:
            nextLevel = []
            for u in queue:
                if u in self.leaves:
                    return u
                seen.add(u)
                for v in self.graph[u]:
                    if v not in seen:
                        nextLevel += [v]
            queue = nextLevel
