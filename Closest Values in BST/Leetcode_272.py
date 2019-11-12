# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(klg(N)) solution
# credit to Stefan Pochmann https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70506/Efficient-Python
class Solution:    
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        def less_equal(root: TreeNode) -> List[int]:
            if root:
                if root.val <= target:
                    for v in less_equal(root.right): yield v
                    yield target - root.val, root.val
                for v in less_equal(root.left): yield v
                    
        def greater(root: TreeNode) -> List[int]:
            if root:
                if root.val > target:
                    for v in greater(root.left): yield v
                    yield root.val - target, root.val
                for v in greater(root.right): yield v
                    
        le, ge = less_equal(root), greater(root)
        merged = heapq. merge(le, ge)
        return [next(merged)[1] for _ in range(k)]

# O(N) solution 
# convert BST into sorted array then do binary search on the array
# class Solution:    
#     def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
#         self.nums = []
        
#         def inorder(node: TreeNode):
#             if not node: return
#             inorder(node.left)
#             self.nums += [node.val]
#             inorder(node.right)
            
#         inorder(root)
        
#         if len(self.nums) <= k: return self.nums
        
#         left, right = 0, len(self.nums) - k
#         while left < right:
#             mid = (left + right)//2
#             if target - self.nums[mid] > self.nums[mid+k] - target:
#                 left = mid +1
#             else:
#                 right = mid
        
#         return self.nums[left: left+k]
    
# O(N) solution using a stack
# top 3%
# class Solution:    
#     def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
#         dq = collections.deque()
#         stack = []
#         while root or stack:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 root = stack.pop()
#                 if len(dq) == k and abs(dq[0] - target) >= abs(root.val - target):
#                     dq.popleft()
#                 if len(dq) < k:
#                     dq.append(root.val)
#                 root = root.right
#         return dq