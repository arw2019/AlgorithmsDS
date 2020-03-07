# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def dfs(cur: 'ListNode', tree: 'TreeNode'):
            if not cur: 
                return True
            elif not tree: 
                return False
            # print(f'list={cur.val}, tree={tree.val}')
            return tree.val == cur.val and (dfs(cur.next, tree.left) or dfs(cur.next, tree.right))
        
        if not head: return True
        if not root: return False
        
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
