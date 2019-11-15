# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# top 3%
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def dfs(node: TreeNode, is_root_node: bool) -> TreeNode:
            if not node: return None
            for_deletion = node.val in to_delete
            if is_root_node and not for_deletion:
                ans.append(node)
            node.left = dfs(node.left, for_deletion)
            node.right = dfs(node.right, for_deletion)
            return None if for_deletion else node
        dfs(root, True)
        return ans
