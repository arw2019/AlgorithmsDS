# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bfs solution

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, j = q.popleft()
            if node:
                d[j]+=[node.val]
                q.append((node.left, j-1))
                q.append((node.right, j+1))
        return [d[j] for j in sorted(d.keys())]
        

# dfs solution

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        self.res = defaultdict(list)
      
        def dfs(node: 'TreeNode', 
                i: """horizontal location: 
                    0 for root, -ve left, +ve right"""
               ) -> None:
            if not node: return
            self.res[i].append(node.val)
            dfs(node.left, i-1)
            dfs(node.right, i+1)
            
        dfs(root, 0)
        
        ans = []
        for vertical_level in sorted(self.res.keys()):
            ans += [self.res[vertical_level]]
            
        return ans
