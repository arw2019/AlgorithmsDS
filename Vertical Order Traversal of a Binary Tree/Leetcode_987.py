# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        self.d = defaultdict(dict)
        self.x_coordinates = set()
        
        def dfs(node: TreeNode, x: int, y: int) -> None:
            if not node: return 
            self.x_coordinates.add(x)
            dfs(node.left, x-1, y+1)
            if y in self.d[x]: 
                self.d[x][y] += [node.val]
            else: 
                self.d[x][y] = [node.val]
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        
        self.x_coordinates = sorted(list(self.x_coordinates))
        ans = []
        for x in self.x_coordinates:
            order = sorted(self.d[x].keys())
            line = []
            for y in order:
                line += sorted(self.d[x][y])
            ans += [line]

        return ans
