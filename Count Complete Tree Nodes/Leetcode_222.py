# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 2.5%
# do binary search the bottom level of the tree
class Solution:
    
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d+=1
        return d
    
    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated 0 to 2**d - 1 (left->right)
        Return true if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d-1
        for _ in range(d):
            pivot = left + (right-left)//2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
    
    def countNodes(self, root: TreeNode) -> int:
        #   if tree is empty
        if not root: return 0
        
        d = self.compute_depth(root)
        # if tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d-1 (left->right)
        #Perform binary search to see how many nodes exist
        left, right = 0, 2**d-1
        while left <= right:
            pivot = left + (right-left)//2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot -1
    
        # The tree contains 2**d-1 nodeson the first (d-1) levels
        #and left nodes on the last level
        return (2**d-1) + left

# AC solution using DFS
# top 30%
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         #to obtain height of tree go down leftmost branch
#         self.h = 0
#         node = root
#         while node:
#             node = node.left
#             self.h += 1
#         self.missing = 0
#         def dfs(node: TreeNode, depth: int):
#             if node: 
#                 dfs(node.left, depth+1)            
#                 dfs(node.right, depth+1)
#             elif depth < self.h: 
#                 self.missing += 1
#         dfs(root, 0)
#         return 2**self.h - 1 - self.missing