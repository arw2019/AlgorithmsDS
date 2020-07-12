class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def helper(node):
            nonlocal max_sum
        
            left_sum = helper(node.left) if node.left else float('-inf') 
            right_sum = helper(node.right) if node.right else float('-inf') 
            through_path = left_sum + right_sum + node.val if node.left and node.right else float('-inf') 
                
            max_sum = max(node.val, 
                          node.val + left_sum, 
                          node.val + right_sum, 
                          through_path, max_sum
            )
            
            max_downward = max(left_sum, right_sum, 0)
            return node.val + max_downward
        
        
        max_sum = float('-inf') 
        if root: 
            helper(root)
        
        return max_sum
